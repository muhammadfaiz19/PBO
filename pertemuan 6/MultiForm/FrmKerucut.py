from tkinter import Frame, Label, Entry, Button, BOTH, END, Tk, W, YES
import math

class FrmKerucut:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Pasang TextBox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=3, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" berfungsi untuk menghitung volume dan luas kerucut
    def onHitung(self, event=None):
        jari_jari = float(self.txtJarijari.get())
        tinggi = float(self.txtTinggi.get())

        # Hitung volume kerucut: V = (1/3) * π * r^2 * t
        volume = (1/3) * math.pi * jari_jari**2 * tinggi

        # Hitung luas kerucut: A = π * r * (r + s), s = sqrt(r^2 + h^2)
        s = math.sqrt(jari_jari**2 + tinggi**2)
        luas = math.pi * jari_jari * (jari_jari + s)

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
    aplikasi = FrmKerucut(root, "Program Volume dan Luas Kerucut")
    root.mainloop()
