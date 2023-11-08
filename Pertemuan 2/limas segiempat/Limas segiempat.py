import tkinter as tk
from tkinter import Frame, Label, Entry, Button,END, W
from math import pi


def hitung_volume():
    p = float(txtpanjang.get())
    T = float(txttinggi.get())
    s = float(txtsisimiring.get())
    
    V = round((1/3) * p * p * T ,2)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    p = float(txtpanjang.get())
    T = float(txttinggi.get())
    s = float(txtsisimiring.get())
    
    lp =  (p*p) + (2*p*s)
    
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
app.title("Menghitung Luas Permukaan dan Volume limas segiempat")

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

# Label panjang
panjang = Label(Frame, text='Panjang Persegi: ')
panjang.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txtpanjang = Entry(Frame)
txtpanjang.grid(row=3, column=1)

# Label tinggi
tinggi = Label(Frame, text='Tinggi limas: ')
tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txttinggi = Entry(Frame)
txttinggi.grid(row=4, column=1)

# Label sisi miring
sisimiring = Label(Frame, text='Sisi Miring: ')
sisimiring.grid(row=5, column=0, sticky=W, padx=5, pady=5)

txtsisimiring = Entry(Frame)
txtsisimiring.grid(row=5, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung, bg="lightblue")
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Label Volume
volume = Label(Frame, text='Volume: ')
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtvolume = Entry(Frame)
txtvolume.grid(row=7, column=1)

# Label Luas Permukaan
luaspermukaan = Label(Frame, text='Luas Permukaan: ')
luaspermukaan.grid(row=8, column=0, sticky=W, padx=5, pady=5)

txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=8, column=1)



app.mainloop()
