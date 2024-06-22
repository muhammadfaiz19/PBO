import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from FrmLogin import *
from FrmMahasiswa import *
from FrmMata_kuliah import *


class Dashboard:
    def __init__(self):
        # Root window
        self.root = tk.Tk()
        self.root.title('Menu Demo')

        # Load background image
        self.bg_image = Image.open("umc.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Set background image
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(relwidth=1, relheight=1)
        
        # Set window size
        self.root.geometry("800x600")

        # Data and level variables
        self.__data = None
        self.__level = None

        # Create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # Create menus
        self.file_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.mahasiswa_menu = Menu(self.menubar)
        self.dosen_menu = Menu(self.menubar)

        # Add menu items to File menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # Add menu items to Admin menu
        self.admin_menu.add_command(label='Tambah Mahasiswa', command=lambda: self.new_window("Tambah Mahasiswa", FormMahasiswa))
        self.admin_menu.add_command(label='Kelola Perwalian', command=lambda: self.new_window("Kelola Perwalian", FormMataKuliah))

        # Add menu items to Dosen menu
        self.dosen_menu.add_command(label='Tambah Mahasiswa', command=lambda: self.new_window("Tambah Mahasiswa", FormMahasiswa))
        self.dosen_menu.add_command(label='Kelola Perwalian', command=lambda: self.new_window("Kelola Perwalian", FormMataKuliah))

        # Add menus to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # Delete login menu
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # Add menu according to level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            elif(level=='mahasiswa'): 
                self.menubar.add_cascade(label="Mahasiswa", menu=self.mahasiswa_menu)
                self.__level = 'Mahasiswa'
            elif(level=='dosen'):
                self.menubar.add_cascade(label="Dosen", menu=self.dosen_menu)
                self.__level = 'Dosen'
            else:
                pass

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
