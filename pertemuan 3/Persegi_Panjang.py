import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    
    L = round(pj * lb)
    
    txtluas.delete(0,END)
    txtluas.insert(END,L)
    
def hitung_keliling():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    
    K = round(2 * (pj + lb))
    
    txtKeliling.delete(0,END)
    txtKeliling.insert(END,K)
    
def hitung():
    hitung_luas()
    hitung_keliling()
    
    
# Create tkinter object
app = tk.Tk()
app.configure(bg='lightblue')

# Atur ukuran window
app.geometry('300x300')

# Tambahkan Judul
app.title("Kalkulator Luas Persegi Panjang")

# Windows
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
panjang.grid(row=3, column=0, sticky=W ,padx=5 ,pady=5)

# Label Lebar
lebar = Label(Frame, text="Lebar : ")
lebar.grid(row=4, column=0, sticky=W ,padx=5 ,pady=5)

# Textbox Panjang
txtpanjang = Entry(Frame)
txtpanjang.grid(row=3, column=1)

# Textbox Lebar
txtlebar = Entry(Frame)
txtlebar.grid(row=4, column=1)

# Button
hitung_button = Button(Frame, text="Hitung", command=hitung, bg = "lightblue")
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(Frame, text="Luas : ")
luas.grid(row=6, column=0, stick=W, padx=5, pady=5)

# Output Label Keliling
keliling = Label(Frame, text="Keliling : ")
keliling.grid(row=7, column=0, stick=W, padx=5, pady=5)


# Output Textbox Luas
txtluas = Entry(Frame)
txtluas.grid(row=6, column=1, stick=W, padx=5, pady=5)

# Output Textbox keliling
txtKeliling = Entry(Frame)
txtKeliling.grid(row=7, column=1, stick=W, padx=5, pady=5)

app.mainloop()