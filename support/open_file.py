from tkinter import filedialog

init_dir = 'C:/Users/akusc/Projects/AIP_Parser'

def open_file():
        file_path = filedialog.askopenfilename(initialdir=init_dir,
            title="Select a file",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if file_path:
            return file_path
        else:
            print("No file selected.")

if __name__ == '__main__':
    open_file()