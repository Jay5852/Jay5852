import os
import sys
from pathlib import Path
import PyPDF2
import pdfplumber

def extract_pdf_text(pdf_path: str) -> str:
    """Extract text from a PDF using PyPDF2, falling back to pdfplumber if needed."""
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = []
            for page in reader.pages:
                txt = page.extract_text()
                if txt:
                    text.append(txt)
            return "\n".join(text)
    except Exception as e:
        # Fallback to pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

def main():
    pdf_dir = r"C:\\Users\\mayur\\Desktop\\New folder (5)"
    pdf_files = [
        "Jay_Dukare_8624965858.pdf",
        "Jay_Dukare_Resume.pdf",
        "Jay_Dukare_Resume_Emd.pdf",
    ]
    for pdf_name in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_name)
        if not os.path.isfile(pdf_path):
            print(f"File not found: {pdf_path}", file=sys.stderr)
            continue
        text = extract_pdf_text(pdf_path)
        txt_path = Path(pdf_path).with_suffix('.txt')
        txt_path.write_text(text, encoding='utf-8')
        print(f"Extracted {pdf_name} -> {txt_path.name}")

if __name__ == "__main__":
    main()
