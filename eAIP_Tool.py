#import os
#from PIL import Image
#from pdf2image import convert_from_path
#import pytesseract
import pymupdf
import tkinter as tk
from support.open_file import open_file

root = tk.Tk()
root.title("eAIP Parser")
root.withdraw() 

file_path = open_file()


doc = pymupdf.open(file_path)
out = open("output.txt", "wb")
for page in doc: 
    text = page.get_text().encode("utf8")
    out.write(text)
    out.write(bytes((12,))) # form feed 0x0C
out.close()


#print(pytesseract.image_to_string(Image.open('test.png')))

#filePath = './RJAA_full.pdf'
#oc = convert_from_path(filePath)
#path, fileName = os.path.split(filePath)
#fileBaseName, fileExtension = os.path.splitext(fileName)

#for page_number, page_data in enumerate(doc):
#    txt = pytesseract.image_to_string(Image.fromarray(page_data)).encode("utf-8")
#    print("Page # {} - {}".format(str(page_number),txt))
