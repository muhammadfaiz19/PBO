from tkinter import Frame, Label, Entry, Button, BOTH, END, Tk, W

class FrmLimasSegiempat:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text='Panjang Alas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Lebar Alas:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=5, column=0, sticky=W, padx=5, pady=5)

        # Pasang TextBox
        self.txtPanjangAlas = Entry(mainFrame) 
        self.txtPanjangAlas.grid(row=0, column=1, padx=5, pady=5)  
        self.txtLebarAlas = Entry(mainFrame) 
        self.txtLebarAlas.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" berfungsi untuk menghitung volume dan luas limas segiempat
    def onHitung(self, event=None):
        panjang_alas = float(self.txtPanjangAlas.get())
        lebar_alas = float(self.txtLebarAlas.get())
        tinggi = float(self.txtTinggi.get())

        # Hitung volume limas segiempat: V = (1/3) * panjang_alas * lebar_alas * tinggi
        volume = (1/3) * panjang_alas * lebar_alas * tinggi

        # Hitung luas limas segiempat: A = panjang_alas * lebar_alas + (panjang_alas * sqrt((lebar_alas/2)^2 + tinggi^2)) + (lebar_alas * sqrt((panjang_alas/2)^2 + tinggi^2))
        luas = panjang_alas * lebar_alas + (panjang_alas * ((lebar_alas/2)**2 + tinggi**2)**0.5) + (lebar_alas * ((panjang_alas/2)**2 + tinggi**2)**0.5)

        # Update entry fields
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, f"{volume:.2f}")

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, f"{luas:.2f}")
               
    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasSegiempat(root, "Program Volume dan Luas Limas Segiempat")
    root.mainloop()
