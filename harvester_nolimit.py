import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import hashlib
from datetime import datetime
import json
import os
import time
from PyPDF2 import PdfReader

def get_document_links(page_url, session):
    """Find all PDF/EPUB/HTML links on the page."""
    response = session.get(page_url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if any(href.lower().endswith(ext) for ext in ['.pdf', '.epub', '.html']):
            links.append((urljoin(page_url, href), link.get_text(strip=True)))
    return links

def download_file(file_url, output_dir, session):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.basename(urlparse(file_url).path) or 'downloaded_file'
    local_path = os.path.join(output_dir, filename)
    with session.get(file_url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_path

def extract_pdf_metadata(local_path):
    try:
        reader = PdfReader(local_path)
        info = reader.metadata
        title = info.get('/Title', '') or os.path.basename(local_path)
        author = info.get('/Author', '')
        creation = info.get('/CreationDate', '')
        pub_year = ''
        if creation and len(creation) >= 6:
            pub_year = creation[2:6]
        return title, author, pub_year
    except Exception:
        return os.path.basename(local_path), '', ''

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def process_site(site_url, output_dir, session):
    links = get_document_links(site_url, session)
    records = []
    domain = urlparse(site_url).netloc
    for doc_url, link_text in links:
        try:
            print(f"Downloading: {doc_url}")
            local_path = download_file(doc_url, output_dir, session)
            checksum = sha256sum(local_path)
            if local_path.lower().endswith('.pdf'):
                title, author, pub_year = extract_pdf_metadata(local_path)
            else:
                title, author, pub_year = link_text, '', ''
            doc_id = f"doc_{hashlib.sha256(doc_url.encode()).hexdigest()[:8]}"
            record = {
                "site": domain,
                "document_id": doc_id,
                "title": title.strip() or link_text,
                "authors": [author] if author else [],
                "pub_year": pub_year,
                "language": "Sanskrit",
                "download_url": doc_url,
                "checksum": checksum,
                "scraped_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            }
            # Save JSON
            json_path = os.path.join(output_dir, f"{doc_id}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(record, f, indent=2, ensure_ascii=False)
            records.append(record)
            time.sleep(1.5)
        except Exception as e:
            print(f"Error processing {doc_url}: {e}")
    return records

if __name__ == "__main__":
    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    sites = [
        "https://sanskritdocuments.org/scannedbooks/asisanskritpdfs.html",
        "https://sanskritdocuments.org/scannedbooks/asiallpdfs.html",
        "https://indianculture.gov.in/ebooks",
        "https://ignca.gov.in/divisionss/asi-books/",
        "https://archive.org/details/TFIC_ASI_Books/ACatalogueOfTheSamskritManuscriptsInTheAdyarLibraryPt.1/",
        "https://indianmanuscripts.com/",
        "https://niimh.nic.in/ebooks/ayuhandbook/index.php"
    ]
    output_dir = "nolimit_output"
    all_records = []
    for site in sites:
        try:
            records = process_site(site, output_dir, session)
            all_records.extend(records)
        except Exception as e:
            print(f"Error processing {site}: {e}")
    with open(os.path.join(output_dir, "summary.json"), 'w', encoding='utf-8') as f:
        json.dump(all_records, f, indent=2, ensure_ascii=False)
    print(f"\nProcessed {len(all_records)} files. Summary saved to {os.path.join(output_dir, 'summary.json')}")
