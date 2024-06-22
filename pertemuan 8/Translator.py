import tkinter as tk
from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x350")  # Menyesuaikan ukuran jendela
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks: ').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Inggris: ').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Spanyol: ').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Turki : ').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)     
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        self.txtHasil1 = Entry(mainFrame, width=50) 
        self.txtHasil1.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtHasil2 = Entry(mainFrame, width=50) 
        self.txtHasil2.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtHasil3 = Entry(mainFrame, width=50) 
        self.txtHasil3.grid(row=4, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!',
            command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=1, padx=5, pady=5) 
        
        # Watermark Brouu
        nama = Label(mainFrame, text="Muhammad Faiz", bg='lightblue')
        nama.grid(row=5, column=1, sticky='nsew' , padx=5, pady=5)
        
        nim = Label(mainFrame, text="220511139", bg='lightblue')
        nim.grid(row=6, column=1, sticky='nsew' , padx=5, pady=5)
        
        kelas = Label(mainFrame, text="TI22D", bg='lightblue')
        kelas.grid(row=7, column=1, sticky='nsew' , padx=5, pady=5)

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil1 = penterjemah.translate(self.txtSumber.get(), src='su', dest='en')  # Bahasa Sunda ke Bahasa Inggris
        hasil2 = penterjemah.translate(self.txtSumber.get(), src='su', dest='es')  # Bahasa Sunda ke Bahasa Spanyol
        hasil3 = penterjemah.translate(self.txtSumber.get(), src='su', dest='tr')  # Bahasa Sunda ke Bahasa Turki
         
        # menampilkan hasil terjemahan
        self.txtHasil1.delete(0, END)
        self.txtHasil1.insert(END, hasil1.text)
        
        self.txtHasil2.delete(0, END)
        self.txtHasil2.insert(END, hasil2.text)
        
        self.txtHasil3.delete(0, END)
        self.txtHasil3.insert(END, hasil3.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()
