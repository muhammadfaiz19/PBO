from tkinter import Frame, Label, Entry, Button, BOTH, END, Tk, W, YES  
import math

class FrmPrismaSegitiga:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text='Alas Segitiga:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Segitiga:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Prisma:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=5, column=0, sticky=W, padx=5, pady=5)

        # Pasang TextBox
        self.txtAlasSegitiga = Entry(mainFrame) 
        self.txtAlasSegitiga.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggiSegitiga = Entry(mainFrame) 
        self.txtTinggiSegitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiPrisma = Entry(mainFrame) 
        self.txtTinggiPrisma.grid(row=2, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" berfungsi untuk menghitung volume dan luas prisma segitiga
    def onHitung(self, event=None):
        alas_segitiga = float(self.txtAlasSegitiga.get())
        tinggi_segitiga = float(self.txtTinggiSegitiga.get())
        tinggi_prisma = float(self.txtTinggiPrisma.get())

        # Hitung volume prisma segitiga: V = (1/2) * alas_segitiga * tinggi_segitiga * tinggi_prisma
        volume = (1/2) * alas_segitiga * tinggi_segitiga * tinggi_prisma

        # Hitung luas prisma segitiga: A = alas_segitiga * tinggi_prisma + (3 * alas_segitiga * tinggi_segitiga)
        luas = alas_segitiga * tinggi_prisma + (3 * alas_segitiga * tinggi_segitiga)

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
    aplikasi = FrmPrismaSegitiga(root, "Program Volume dan Luas Prisma Segitiga")
    root.mainloop()
