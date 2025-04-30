Sanskrit Document Metadata Harvester
This repository provides two Python scripts for harvesting and structuring metadata from Sanskrit document repositories:

harvester_nolimit.py: Downloads and processes all matching files (PDF/EPUB/HTML) from each target website.

harvester_onelimit.py: Downloads and processes only the first matching file from each target website.

Features
Web crawling with polite delays and browser-like headers

File downloading (PDF/EPUB/HTML)

Metadata extraction: title, author/editor, publication year, language, unique document ID, SHA-256 checksum

JSON output: One record per document, normalized as per assignment requirements

Summary file: Aggregated JSON for all processed records

Error handling and logging

File Structure
harvester_nolimit.py - No limit, processes all files per site

harvester_onelimit.py - One file per site

nolimit_output/ or onelimit_output/ - Output folders for downloaded files and JSON records

summary.json - Aggregated summary of all records in the output folder

JSON Record Example
json
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
How to Use
1. Install Dependencies
bash
pip install requests beautifulsoup4 PyPDF2
2. Run the Script
To process all files per site:

bash
python harvester_nolimit.py
To process only the first file per site:

bash
python harvester_onelimit.py
3. Output
Downloaded files and their JSON records are saved in the output folder.

A summary.json file contains all records for easy review.
