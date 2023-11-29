import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luasPermukaaan():
    s = float(txtsisi.get())

    L = round(6 * s**2)
    txtluasPermukaaan.delete(0, END)
    txtluasPermukaaan.insert(END,L)

def hitung_volume():
    s = float(txtsisi.get())
    
    V = round(s**3)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luasPermukaaan()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()
app.configure(bg='lightblue')

# Atur ukuran window
app.geometry('300x300')

# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Volume Kubus")

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

# Label Sisi
sisi = Label(Frame, text="Sisi : ")
sisi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox sisi
txtsisi = Entry(Frame)
txtsisi.grid(row=3, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung, bg="lightblue")
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luasPermukaaan = Label(Frame, text="Luas Permukaaan : ")
luasPermukaaan.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(Frame, text="Volume : ")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)


# Output Textbox luasPermukaaan
txtluasPermukaaan = Entry(Frame)
txtluasPermukaaan.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry(Frame)
txtvolume.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()