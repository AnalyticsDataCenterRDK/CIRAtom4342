from tkinter import *
from tkinter import filedialog as fd

#ganglp;egT8FETG[P;]
def data_upload():
    def insert_text():
        file_name = fd.askopenfilename()
        f = open(file_name, encoding='utf-8')
        s = f.read()
        text.insert(1.0, s)
        f.close()

    def extract_text():
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("DB files", "*.db"),
                       ("CSV files", "*.csv"),
                       ("XLSX files", "*.xlsx"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()

    data_upload_root = Tk()
    data_upload_root.geometry("1000x500")
    data_upload_root.title("C.I.R Atom Data Upload")

    text = Text(width=50, height=25)
    text.grid(columnspan=2)

    b1 = Button(text="Открыть", command=insert_text)
    b1.grid(row=1, sticky=E)

    b2 = Button(text="Сохранить", command=extract_text)
    b2.grid(row=1, column=1, sticky=W)