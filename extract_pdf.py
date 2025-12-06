#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

# Install PyMuPDF if needed
try:
    import fitz
    print("PyMuPDF already installed")
except ImportError:
    print("Installing PyMuPDF...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "PyMuPDF"])
    print("✓ PyMuPDF installed")

# Now run the conversion
pdf_path = "/workspaces/Virtual-Operating-Layer/docs/research/sythetic machinery.pdf"
output_path = "/workspaces/Virtual-Operating-Layer/docs/research/sythetic machinery.md"

import fitz

print(f"\nExtracting text from PDF...")
doc = fitz.open(pdf_path)
all_text = []

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    if text.strip():
        all_text.append(text)

doc.close()

# Write raw extraction first
raw_output = Path(output_path.replace('.md', '_raw.txt'))
raw_output.write_text("\n\n".join(all_text), encoding='utf-8')
print(f"✓ Raw extraction saved to: {raw_output}")
print(f"  Pages extracted: {len(all_text)}")
print(f"  Total characters: {sum(len(t) for t in all_text)}")

# Now we can format it properly
print("\nRaw text extracted. Ready for formatting...")
