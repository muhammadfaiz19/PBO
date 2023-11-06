import tkinter as tk
from tkinter import Frame, Label, Entry, Button,END, W
from math import pi


def hitung_volume():
    a = float(txtalas.get())
    T = float(txtTinggi.get())
    t = float(txttinggi.get())
    s = float(txtsisitegak.get())
    
    V = round((1/2)*a*t*T,2)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    a = float(txtalas.get())
    T = float(txtTinggi.get())
    t = float(txttinggi.get())
    s = float(txtsisitegak.get())
    
    lp =  ((s+s+a)*T)+a*t
    
    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,lp)

def hitung():
    hitung_volume()
    hitung_luaspermukaan()
    
# Create tkinter object app = tk.Tk()
app = tk.Tk()
app.configure(bg='lightblue')

# Atur ukuran window
app.geometry('300x300')

# Tambahkan judul
app.title("Program Menghitung volume dan luas permukaan prisma segitiga")

# windows
Frame = Frame(app)
Frame.pack(padx=30, pady=30)

# Label Nama
nama = Label(Frame, text="Muhammad Faiz")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label NIM
NIM = Label(Frame, text="220511139")
NIM.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Kelas
Kelas = Label(Frame, text="TI22D")
Kelas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Alas
alas = Label(Frame, text="Alas : ")
alas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi prisma
Tinggi = Label(Frame, text="Tinggi  prisma: ")
Tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Tingi Segitiga
tinggi = Label(Frame, text="Tinggi Segitiga alas : ")
tinggi.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Sisi miring segitiga
sisimiring = Label(Frame, text="Sisi Miring segitiga : ")
sisimiring.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Label Volume
volume = Label(Frame, text="Volume : ")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Label Luas Permukaan
luaspermukaan = Label(Frame, text="Luas Permukaan")
luaspermukaan.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung, bg="lightblue")
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Textbox Alas
txtalas = Entry(Frame)
txtalas.grid(row=3, column=1)

# Textbox tinggi prisma
txtTinggi = Entry(Frame)
txtTinggi.grid(row=4, column=1)

# Textbox tinggi segitiga
txttinggi = Entry(Frame)
txttinggi.grid(row=5, column=1)

# Textbox Sisi Tegak
txtsisitegak = Entry(Frame)
txtsisitegak.grid(row=6, column=1)

# textbox volume
txtvolume = Entry(Frame)
txtvolume.grid(row=8, column=1)

# Textbox Luas Permukaan
txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=9, column=1)

app.mainloop()

