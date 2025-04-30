# 📚 Sanskrit Document Metadata Harvester

A robust Python toolkit for crawling, downloading, and structuring metadata from Sanskrit document repositories. Designed to fulfill the requirements of the Data Harvesting & Structuring Assignment.

## ✨ Features

- **Web crawling** with browser-like headers and polite delays
- **Flexible file handling:**
  - `harvester_nolimit.py`: Download **all** matching files per website
  - `harvester_onelimit.py`: Download **only the first** matching file per website
- **Metadata extraction:** Title, author/editor, publication year, language, unique document ID, SHA-256 checksum, download URL, scrape timestamp
- **JSON output:** One record per document, normalized fields (ISO 8601 dates, consistent author formatting)
- **Summary file:** Aggregated JSON for all processed records
- **Error handling** and logging

## 🗂️ File Structure

```
project-root/
│
├── harvester_nolimit.py      # Processes all matching files per website
├── harvester_onelimit.py     # Processes only the first matching file per website
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

## 🚦 How to Use

### 1. Install Dependencies

```
pip install requests beautifulsoup4 PyPDF2
```

### 2. Run the Script

- **To process all files per site:**
  ```
  python harvester_nolimit.py
  ```
- **To process only the first file per site:**
  ```
  python harvester_onelimit.py
  ```

### 3. Output

- Downloaded files and JSON records are saved in the corresponding output folders.
- A `summary.json` file contains all records for easy review.

## 🛠️ Notes & Best Practices

- **Polite crawling:** 1.5–2 second delay between downloads to respect server load.
- **Browser-like headers:** Avoids 406 errors and blocks.
- **PDF metadata:** Only basic fields are extracted; EPUB/HTML metadata extraction can be added similarly.
- **OCR/text extraction:** Not included in this version, but hooks can be added for Tesseract or Apache Tika.
- **Delta processing:** Not included in this version; can be added using checksums and last-modified headers.

