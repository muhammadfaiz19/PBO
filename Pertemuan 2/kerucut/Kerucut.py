import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

def hitung_volume():
    r = float(txtjari_jari.get())
    T = float(txttinggi.get())
    s = float(txtgarisPelukis.get())
    
    V = round((1/3) * pi * r  * r * T,2)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    r = float(txtjari_jari.get())
    T = float(txttinggi.get())
    s = float(txtgarisPelukis.get())
    
    
    lp = round(pi * r * (s + r),2)
    
    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,lp)

def hitung():
    hitung_volume()
    hitung_luaspermukaan()
    

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Atur ukuran window
app.geometry('300x300')
app.configure(bg='lightblue')


# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Volume Kerucut")

# windows
Frame = Frame(app)
Frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(Frame, text="Muhammad Faiz")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label NIM
NIM = Label(Frame, text="220511139")
NIM.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Kelas
Kelas = Label(Frame, text="TI22D")
Kelas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Jari-Jari
jari_jari = Label(Frame, text="Jari-Jari")
jari_jari.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(Frame, text="Tinggi")
tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Garis pelukis
garisPelukis = Label(Frame, text="garis pelukis : ")
garisPelukis.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari-Jari
txtjari_jari = Entry(Frame)
txtjari_jari.grid(row=3, column=1)

# Textbox Tinggi
txttinggi = Entry(Frame)
txttinggi.grid(row=4, column=1)

# Textbox Garis Pelukis
txtgarisPelukis = Entry(Frame)
txtgarisPelukis.grid(row=5, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung)
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luaspermukaan = Label(Frame, text="Luas Permukaan: ")
luaspermukaan.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(Frame, text="Volume: ")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry(Frame)
txtvolume.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()