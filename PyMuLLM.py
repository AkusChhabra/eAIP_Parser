import pymupdf4llm
import pathlib
import tkinter as tk
from support.open_file import open_file

root = tk.Tk()
root.title("eAIP Parser")
root.withdraw() 

file_path = open_file()

md_text = pymupdf4llm.to_markdown(file_path)

pathlib.Path("output.md").write_bytes(md_text.encode())