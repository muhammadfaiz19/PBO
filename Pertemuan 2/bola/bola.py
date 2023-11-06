import tkinter as tk
from tkinter import Frame, Label, Entry, Button,END, W
from math import pi


def hitung_volume():
    r = float(txtjarijari.get())
    
    V = round((4/3) * pi * r**3 ,2)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    r = float(txtjarijari.get())
    
    lp = round(4*pi*r*r,2)
    
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
app.title("Program Menghitung volume dan luas permukaan bola")

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

# Label jari jari
jarijari = Label(Frame, text='jari - jari : ')
jarijari.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox jari jari
txtjarijari = Entry(Frame)
txtjarijari.grid(row=3, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung, bg="lightblue")
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Label Volume
volume = Label(Frame, text='Volume : ')
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Label Luas Permukaan
lp = Label(Frame, text='Luas Permukaan : ')
lp.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Textbox Volume
txtvolume = Entry(Frame)
txtvolume.grid(row=5, column=1)

# Textbox Luas Permukaan
txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=6, column=1)


app.mainloop()

