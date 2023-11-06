import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    p = float(txtpanjang.get())
    l  = float(txtlebar.get())
    t = float(txttinggi.get())

    L = round(2 * ( p*l + p*t + l*t))
    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    p = float(txtpanjang.get())
    l  = float(txtlebar.get())
    t = float(txttinggi.get())
    
    V = round(p* l * t)

    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Atur ukuran window
app.geometry('300x300')
app.configure(bg='lightblue')


# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Volume Balok")

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

# Label Panjang
panjang = Label(Frame, text="Panjang : ")
panjang.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar = Label(Frame, text="Lebar : ")
lebar.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(Frame, text="Tinggi : ")
tinggi.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Textbox panjang
txtpanjang = Entry(Frame)
txtpanjang.grid(row=3, column=1)

# Textbox Lebar
txtlebar = Entry(Frame)
txtlebar.grid(row=4, column=1)

# Textbox Tinggix
txttinggi = Entry(Frame)
txttinggi.grid(row=5, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung)
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(Frame, text="Luas : ")
luas.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(Frame, text="Volume : ")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtLuas = Entry(Frame)
txtLuas.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry(Frame)
txtvolume.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()