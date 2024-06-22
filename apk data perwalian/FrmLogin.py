import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from Users import Users

class FormLogin:
    
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.update_main_window = update_main_window 
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        # Membuat frame untuk menampung semua widget
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)  # Mem-packing frame untuk mengisi jendela induk

        # Mendapatkan dimensi layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()

        # Menghitung posisi untuk memusatkan jendela
        x = (screen_width - 800) // 2  # Lebar disesuaikan menjadi 400
        y = (screen_height - 600) // 2  # Tinggi disesuaikan menjadi 200

        # Mendefinisikan lebar dan tinggi jendela
        width = 800
        height = 600

        # Menetapkan geometri jendela
        self.parent.geometry(f"{width}x{height}+{x}+{y}")

        # Menambahkan latar belakang dengan gambar
        self.add_background(mainFrame)

        # Membuat dan menempatkan label Email
        Label(mainFrame, text='Email:', bg="#C2C2C2").place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        # Membuat widget masukan Email dan membuatnya memperluas secara vertikal dan horizontal untuk menyejajarkan ke tengah
        self.txtEmail = Entry(mainFrame, width=20, font=('serif', 14), bd=2, relief=tk.GROOVE, bg='#EAEAEA')
        self.txtEmail.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Membuat dan menempatkan label Password
        Label(mainFrame, text='Password:', bg="#C2C2C2").place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        # Membuat widget masukan Password dan membuatnya memperluas secara vertikal dan horizontal untuk menyejajarkan ke tengah
        self.txtPassword = Entry(mainFrame, width=20, font=('serif', 14), bd=2, relief=tk.GROOVE,  bg='#EAEAEA')
        self.txtPassword.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Membuat dan menempatkan tombol Submit
        self.btnSubmit = Button(mainFrame, text='Login', command=self.onSubmit, width=31, bg="#C2C2C2")
        self.btnSubmit.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        # Membuat dan menempatkan tombol Batal
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onKeluar, width=31, bg="#C2C2C2")
        self.btnCancel.place(relx=0.5, rely=0.61, anchor=tk.CENTER)


    def add_background(self, frame):
        # Mengatur gambar latar belakang
        image_path = "umc.jpg"
        image = Image.open(image_path)
        darkened_image = ImageEnhance.Brightness(image).enhance(0.5)  # Mengurangi kecerahan gambar
        photo = ImageTk.PhotoImage(darkened_image)
        
        # Menampilkan gambar latar belakang di frame
        bg_label = Label(frame, image=photo)
        bg_label.image = photo  # Penting agar gambar tidak dihapus oleh garbage collector
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def onSubmit(self, event=None):
        email = self.txtEmail.get()
        password = self.txtPassword.get()
                
        obj = Users()
        val = obj.Validasi(email, password)
        C = val[1]
        if C == True:
            self.update_main_window(val)
            self.parent.destroy()
        else:
            messagebox.showwarning("showwarning", "Login Gagal ")
    
        return val

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

    
if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = FormLogin(root, "Aplikasi Data Login", update_main_window)
    root.mainloop()
