#!/usr/bin/env python3
"""
PDF to Markdown Converter
Extracts text from PDF and converts to clean markdown format
"""

import sys
import re
from pathlib import Path

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

try:
    from pdfminer.high_level import extract_text as pdfminer_extract
    HAS_PDFMINER = False
except ImportError:
    HAS_PDFMINER = False

def extract_text_pymupdf(pdf_path):
    """Extract text using PyMuPDF (fitz)"""
    doc = fitz.open(pdf_path)
    text_blocks = []
    
    for page_num, page in enumerate(doc, 1):
        text = page.get_text()
        if text.strip():
            text_blocks.append(text)
    
    return "\n\n".join(text_blocks)

def extract_text_pdfminer(pdf_path):
    """Extract text using pdfminer.six"""
    return pdfminer_extract(pdf_path)

def clean_text(text):
    """Clean up extracted text"""
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove page numbers (common patterns)
    text = re.sub(r'\n\d+\n', '\n', text)
    return text.strip()

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """Convert PDF to markdown"""
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        return False
    
    # Determine output path
    if output_path is None:
        output_path = pdf_path.with_suffix('.md')
    else:
        output_path = Path(output_path)
    
    print(f"Converting: {pdf_path}")
    print(f"Output to: {output_path}")
    
    # Extract text
    try:
        if HAS_PYMUPDF:
            print("Using PyMuPDF for extraction...")
            raw_text = extract_text_pymupdf(str(pdf_path))
        elif HAS_PDFMINER:
            print("Using pdfminer.six for extraction...")
            raw_text = extract_text_pdfminer(str(pdf_path))
        else:
            print("Error: No PDF extraction library available")
            print("Please install: pip install PyMuPDF")
            return False
    except Exception as e:
        print(f"Error extracting text: {e}")
        return False
    
    # Clean the text
    cleaned_text = clean_text(raw_text)
    
    # Write to file
    try:
        output_path.write_text(cleaned_text, encoding='utf-8')
        print(f"✓ Conversion complete: {output_path}")
        return True
    except Exception as e:
        print(f"Error writing output: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_md_converter.py <pdf_file> [output_file]")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = convert_pdf_to_markdown(pdf_file, output_file)
    sys.exit(0 if success else 1)
