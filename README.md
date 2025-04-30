```markdown
# 📚 Sanskrit Document Metadata Harvester

A Python toolkit for crawling, downloading, and structuring metadata from Sanskrit document repositories. This project is designed to fulfill the requirements of the [Data Harvesting & Structuring Assignment](Data-Harvesting-Structuring-Assignment.pdf).

---

## 🚀 Features

- **Web crawling** with polite delays and browser-like headers
- **Flexible file handling:**  
  - `harvester_nolimit.py`: Download **all** matching files per website  
  - `harvester_onelimit.py`: Download **only the first** matching file per website
- **Metadata extraction**:  
  - Title  
  - Author/editor  
  - Publication year  
  - Language  
  - Unique document ID  
  - SHA-256 checksum  
  - Download URL  
  - Scrape timestamp
- **JSON output**:  
  - One record per document  
  - Normalized fields (ISO 8601 dates, consistent author formatting)
- **Summary file**:  
  - Aggregated JSON for all processed records
- **Error handling** and logging

---

## 🗂️ File Structure

```
project-root/
│
├── harvester_nolimit.py      # Processes all matching files per website
├── harvester_onelimit.py     # Processes only the first matching file per website
├── Data-Harvesting-Structuring-Assignment.pdf
│
├── nolimit_output/           # Output for harvester_nolimit.py
│   ├── 
│   ├── 
│   └── summary.json
│
└── onelimit_output/          # Output for harvester_onelimit.py
    ├── 
    ├── 
    └── summary.json
```

---

## 📝 JSON Record Example

```
{
  "site": "ayushportal.nic.in",
  "document_id": "doc1234abcd",
  "title": "Ancient Text on Ayurveda",
  "authors": ["Name Surname"],
  "pub_year": "1998",
  "language": "Sanskrit",
  "download_url": "https://.../doc1234.pdf",
  "checksum": "a1b2c3...",
  "scraped_at": "2025-04-26T10:15:00Z"
}
```

---

## ⚙️ Installation

1. **Clone the repository** and navigate to the directory.
2. **Install dependencies:**

   ```
   pip install requests beautifulsoup4 PyPDF2
   ```

---

## 🏃 Usage

### To process **all files** per site:

```
python harvester_nolimit.py
```

### To process **only the first file** per site:

```
python harvester_onelimit.py
```

- Downloaded files and JSON records are saved in the corresponding output folders.
- A `summary.json` file contains all records for easy review.

---

## 🌐 Target Websites

The scripts are pre-configured to crawl the following sources (as per assignment):

- https://sanskritdocuments.org/scannedbooks/asisanskritpdfs.html
- https://sanskritdocuments.org/scannedbooks/asiallpdfs.html
- https://indianculture.gov.in/ebooks
- https://ignca.gov.in/divisionss/asi-books/
- https://archive.org/details/TFIC_ASI_Books/ACatalogueOfTheSamskritManuscriptsInTheAdyarLibraryPt.1/
- https://indianmanuscripts.com/
- https://niimh.nic.in/ebooks/ayuhandbook/index.php

You can edit the `sites` list in either script to add or remove sources.

---

## 🧪 Test Cases

| Test Case                  | Input/Action                                | Expected Outcome                                      |
|----------------------------|---------------------------------------------|-------------------------------------------------------|
| TC1: Crawl Basic Page      | Run crawler on a sample site                | HTML saved, PDF links identified and downloaded       |
| TC2: Metadata JSON         | Process a sample PDF                        | JSON record with all required fields, correct formats |
| TC3: OCR Extraction        | (Future: for scanned PDFs)                  | `content` field contains OCR-extracted text           |
| TC4: Checksum & Delta      | Modify and re-run                           | Script flags changed file, re-processes it            |
| TC5: JSON Schema Validation| Validate JSON output                        | All records pass schema validation                    |

---

## 🛠️ Notes & Trade-offs

- **Polite crawling:** 1.5–2 second delay between downloads to respect server load.
- **Browser-like headers:** Avoids 406 errors and blocks.
- **PDF metadata:** Only basic fields are extracted; EPUB/HTML metadata extraction can be added similarly.
- **OCR/text extraction:** Not included in this version, but hooks can be added for Tesseract or Apache Tika.
- **Delta processing:** Not included in this version; can be added using checksums and last-modified headers.

---
