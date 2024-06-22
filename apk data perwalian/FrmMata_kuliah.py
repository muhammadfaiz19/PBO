import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, StringVar, messagebox
from Mata_kuliah import Mata_kuliah
from Mahasiswa import Mahasiswa
from tkcalendar import Calendar, DateEntry

class FormMataKuliah:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.update_main_window = update_main_window       
        self.parent.geometry("1000x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_keluar)
        
        self.ditemukan = None
        self.atur_komponen()
        self.on_reload()
        
    def atur_komponen(self):
        main_frame = Frame(self.parent, bd=10, bg="#34353D")
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Combo Box MAHASISWA
        Label(main_frame, text='MAHASISWA:', bg="#C2C2C2").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        mahasiswa_data = self.get_mahasiswa_data() 
        self.txtMAHASISWA_ID = ttk.Combobox(main_frame, width=17, values=[nama_mahasiswa for _, nama_mahasiswa in mahasiswa_data])
        self.txtMAHASISWA_ID.grid(row=0, column=1, padx=5, pady=5)
        
        # Combo Box NAMA_MK
        Label(main_frame, text='NAMA_MK:', bg="#C2C2C2").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.txtNAMA_MK = StringVar()
        cboNAMA_MK = ttk.Combobox(main_frame, width=17, textvariable=self.txtNAMA_MK) 
        cboNAMA_MK.grid(row=1, column=1, padx=5, pady=5)
        cboNAMA_MK['values'] = ('Pemrograman Berorientasi Objek', 'AIK', 'Arsitektur dan Organisasi Komputer', 'Sistem Informasi', 'Kalkulus II', 'Komunikasi Data', 'Statistika Dan Probabilitas', 'Struktur Data dan Algoritma')
        cboNAMA_MK.current()
        
        # Combo Box SKS
        Label(main_frame, text='SKS:', bg="#C2C2C2").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.txtSKS = StringVar()
        cboSKS = ttk.Combobox(main_frame, width=17, textvariable=self.txtSKS) 
        cboSKS.grid(row=2, column=1, padx=5, pady=5)
        cboSKS['values'] = ('1', '2', '3', '4', '5', '6')
        cboSKS.current()
        
        # Date Entry
        Label(main_frame, text='DATE:', bg="#C2C2C2").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.txtDATE = DateEntry(main_frame, width=16, background="magenta3", foreground="white", bd=2, date_pattern='y-mm-dd') 
        self.txtDATE.grid(row=3, column=1, padx=5, pady=5)
                    
        # Buttons
        self.btnSimpan = Button(main_frame, text='Simpan', command=self.on_simpan, width=10, bg="#C2C2C2")
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(main_frame, text='Clear', command=self.on_clear, width=10, bg="#C2C2C2")
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(main_frame, text='Hapus', command=self.on_delete, width=10, bg="#C2C2C2")
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # Treeview
        columns = ('mahasiswa_id', 'nama_mk', 'sks', 'date')  # Remove 'id' from columns
        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings', style="Custom.Treeview")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200)  # Adjust the width for other columns
        self.tree.place(x=0, y=250)
        self.on_reload()
        
        # Set warna latar belakang kolom tree
        style = ttk.Style()
        style.theme_use("clam")  # Menggunakan tema "clam"
        style.configure("Custom.Treeview", background="#C2C2C2", fieldbackground="#C2C2C2", foreground="black", rowheight=25)

        self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)
    
    def on_clear(self, event=None):
        self.txtMAHASISWA_ID.set("")
        self.txtNAMA_MK.set("")
        self.txtSKS.set("")
        self.btnSimpan.config(text="Simpan")
        self.on_reload()
        self.ditemukan = False
        
    def get_mahasiswa_data(self):
        dt = Mahasiswa()
        res = dt.getComboData()
        return res 
    
    def sort_by_mahasiswa_id(self):
        self.tree.sort_column('mahasiswa_id')

    def on_reload(self, event=None):
        obj = Mata_kuliah()
        result = obj.getAllData()
        sorted_result = sorted(result, key=lambda x: x[1])  # Urutkan berdasarkan mahasiswa_id
        # Clear existing data in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insert new data into the treeview
        for row_data in sorted_result:
            self.tree.insert('', END, values=row_data[1:])  # Exclude the 'id' column

    def on_item_selected(self, event):
        # Set self.ditemukan to True when an item is selected
        self.ditemukan = True
            
    def on_simpan(self, event=None):
        mahasiswa_id = self.txtMAHASISWA_ID.get()
        nama_mk = self.txtNAMA_MK.get()
        sks = self.txtSKS.get()
        date = self.txtDATE.get()       
        obj = Mata_kuliah()
        obj.mahasiswa_id = mahasiswa_id
        obj.nama_mk = nama_mk
        obj.sks = sks
        obj.date = date
        if self.ditemukan:
            res = obj.updateBy()
            ket = 'Diperbarui'
        else:
            res = obj.simpan()
            ket = 'Disimpan'
        rec = obj.affected
        if rec > 0:
            messagebox.showinfo("showinfo", f"Data Berhasil {ket}")
        else:
            messagebox.showwarning("showwarning", f"Data Gagal {ket}")
        self.on_clear()
        return rec

    def on_delete(self, event=None):
        selected_item = self.tree.selection()
        if selected_item:
            data = self.tree.item(selected_item)['values']
            mahasiswa_id = data[0]
            nama_mk = data[1]
            obj = Mata_kuliah()
            res = obj.deleteBy(mahasiswa_id, nama_mk)
            if res is not None and res > 0:
                messagebox.showinfo("showinfo", "Data Berhasil dihapus")
                self.on_clear()
            else:
                messagebox.showwarning("showwarning", "Operasi penghapusan gagal")
        else:
            messagebox.showinfo("showinfo", "Pilih data yang ingin dihapus")

    def on_keluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMataKuliah(root, "Aplikasi Data Mata_kuliah")
    root.configure(bg="#34353D")  # Ganti warna background root window
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Custom.Treeview", background="#34353D", fieldbackground="#34353D", foreground="white", font=('Arial', 10))
    root.mainloop()
