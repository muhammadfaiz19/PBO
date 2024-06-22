import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Mahasiswa import Mahasiswa

class FormMahasiswa:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg="#34353D")  # Ganti warna background
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # int 
        Label(mainFrame, text='NIM:', bg="#C2C2C2").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NIM
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
                
        # varchar 
        Label(mainFrame, text='NAMA:', bg="#C2C2C2").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=1, column=1, padx=5, pady=5)
                
        # enum 
        Label(mainFrame, text='SEMESTER:', bg="#C2C2C2").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtSEMESTER = StringVar()
        CboSEMESTER = ttk.Combobox(mainFrame, width=17, textvariable=self.txtSEMESTER) 
        CboSEMESTER.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboSEMESTER['values'] = ('1','2','3','4','5','6','7','8')
        CboSEMESTER.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg="#C2C2C2")  # Ganti warna button
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg="#C2C2C2")  # Ganti warna button
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg="#C2C2C2")  # Ganti warna button
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # Define columns
        columns = ('id','nim','nama','semester')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', style="Custom.Treeview")
        # Define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width=50)  # Mengatur lebar kolom 'id' menjadi 50 piksel
        self.tree.heading('nim', text='nim')
        self.tree.column('nim', width=100)  # Mengatur lebar kolom 'nim' menjadi 100 piksel
        self.tree.heading('nama', text='nama')
        self.tree.column('nama', width=150)  # Mengatur lebar kolom 'nama' menjadi 150 piksel
        self.tree.heading('semester', text='semester')
        self.tree.column('semester', width=100)  # Mengatur lebar kolom 'semester' menjadi 100 piksel
        # Set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
        
        # Set warna latar belakang kolom tree
        style = ttk.Style()
        style.theme_use("clam")  # Menggunakan tema "clam"
        style.configure("Custom.Treeview", background="#C2C2C2", fieldbackground="#C2C2C2", foreground="black", rowheight=25)
    
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
                                
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,"")
                                
        self.txtSEMESTER.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # Get data mahasiswa
        obj = Mahasiswa()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        obj = Mahasiswa()
        res = obj.getByNIM(nim)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        obj = Mahasiswa()
        res = obj.getByNIM(nim)
            
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,obj.nama)
                                
        self.txtSEMESTER.set(obj.semester)
            
        self.btnSimpan.config(text="Update")
        
    def onSimpan(self, event=None):
        nim = self.txtNIM.get()
        nama = self.txtNAMA.get()
        semester = self.txtSEMESTER.get()       
        obj = Mahasiswa()
        obj.nim = nim
        obj.nama = nama
        obj.semester = semester
        if(self.ditemukan==True):
            res = obj.updateByNIM(nim)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        nim = self.txtNIM.get()
        obj = Mahasiswa()
        obj.nim = nim
        if(self.ditemukan==True):
            res = obj.deleteByNIM(nim)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()

    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMahasiswa(root, "Aplikasi Data Mahasiswa")
    root.configure(bg="#34353D")  # Ganti warna background root window
    root.mainloop()
