# PDF to JSON Converter

This Python script allows you to convert specific pages of a PDF into a JSON file. It extracts both table data and plain text from the specified pages, making it useful for analyzing and processing PDF content.

## Features

- Extract tables from the PDF using `camelot`.
- Extract text from the PDF using `pdfplumber`.
- Specify page ranges in a flexible format, e.g., `1,2,3` or `1-5`.
- Output data in JSON format for easy integration with other applications.

## Requirements

Make sure you have Python installed and the following libraries:

- `camelot-py[cv]`
- `pdfplumber`
- `json` (standard library)

You can install the required libraries with the following command:
```bash
pip install camelot-py[cv] pdfplumber

