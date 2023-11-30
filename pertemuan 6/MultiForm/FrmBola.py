from tkinter import Frame, Label, Entry, Button, BOTH, END, Tk, W, YES
import math

class FrmBola:
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
        Label(mainFrame, text='Volume:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=3, column=0, sticky=W, padx=5, pady=5)

        # Pasang TextBox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=2, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
        
    # Fungsi "onHitung" berfungsi untuk menghitung volume dan luas bola
    def onHitung(self, event=None):
        jari_jari = float(self.txtJarijari.get())

        # Hitung volume bola: V = (4/3) * π * r^3
        volume = (4/3) * math.pi * jari_jari**3

        # Hitung luas bola: A = 4 * π * r^2
        luas = 4 * math.pi * jari_jari**2

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
    aplikasi = FrmBola(root, "Program Volume dan Luas Bola")
    root.mainloop()
