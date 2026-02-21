from docling.document_converter import DocumentConverter
import tkinter as tk
from support.open_file import open_file

root = tk.Tk()
root.title("eAIP Parser")
root.withdraw() 

file_path = open_file()

file_path = "C:/Users/akusc/Projects/AIP_Parser/RJAA_full.pdf"

converter = DocumentConverter()
doc = converter.convert(file_path).document

markdown_text = doc.document.export_to_markdown()

output_file_path = "output_document.md" # Or "output_document.txt"

# Save the Markdown content to a file
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(markdown_text)

print(f"Markdown content saved to {output_file_path}")

#print(doc.export_to_markdown())