import tkinter as tk
from tkinter import Frame, Label, Entry, Button,END, W
from math import pi


def hitung_volume():
    r = float(txtjarijari.get())
    T = float(txttinggi.get())

    V = round(pi*r*r*T, 2)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    r = float(txtjarijari.get())
    T = float(txttinggi.get())
    
    lp = round(2*pi*r*(T + r),2)
    
    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,lp)

def hitung():
    hitung_volume()
    hitung_luaspermukaan()
    
# Create tkinter object app = tk.Tk()
app = tk.Tk()
app.configure(bg='lightblue')

# Tambahkan judul
app.title("Program Menghitung volume dan luas permukaan tabung")

# Atur ukuran window
app.geometry('300x300')

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

# Label Jari Jari
jarijari = Label(Frame, text='jari- jari : ')
jarijari.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari Jari
txtjarijari = Entry(Frame)
txtjarijari.grid(row=3, column=1)

# Label Tinggi 
tinggi = Label(Frame, text='Tinggi : ')
tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Textbox TInggi
txttinggi = Entry(Frame)
txttinggi.grid(row=4, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung, bg="lightblue")
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Lebel Volume
volume = Label(Frame, text='Volume : ')
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(Frame)
txtvolume.grid(row=6, column=1)

# Output Luas Permukaan
lp = Label(Frame, text='Luas Permukaan : ')
lp.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=7, column=1)


app.mainloop()

