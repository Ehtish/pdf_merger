# PDF Merger

A simple Python automation tool that combines multiple PDF files into one PDF.

## Description

The program reads PDF files from a folder and merges them into a single `combined.pdf` file.

## Requirements

- Python 3
- PyPDF2

Install:

```bash
pip install PyPDF2
```

## Project Flow

```text
PDF Files
   ↓
Read Files
   ↓
Check .pdf
   ↓
Add PDF to Merger
   ↓
Merge All PDFs
   ↓
Save combined.pdf
```

## Example

### Before

```text
pdf_merger/
├── main.py
├── pdf_files/
│   ├── file_1.pdf
│   ├── file_2.pdf
│   └── file_3.pdf
└── output/
```

### After

```text
output/
└── combined.pdf
```

The pages from all input PDFs are included in `combined.pdf` in sequence.

## Concepts Practiced

- Python modules
- External libraries
- PyPDF2
- os.listdir()
- os.path.join()
- os.makedirs()
- for loop
- File extension checking
- PDF merging
- File paths

## Project Structure

```text
pdf_merger/
├── main.py
├── pdf_files/
└── output/
```

## Quick Recap

```text
Multiple PDFs → Add to merger → Merge → Save combined.pdf
```

This project was built to practice Python-based PDF automation.
