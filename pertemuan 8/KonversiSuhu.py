import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temperature * 9/5) + 32
            elif to_unit == "Reamur":
                result = temperature * 4/5
            elif to_unit == "Kelvin":
                result = temperature + 273.15

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temperature - 32) * 5/9
            elif to_unit == "Reamur":
                result = (temperature - 32) * 5/9 * 4/5
            elif to_unit == "Kelvin":
                result = (temperature - 32) * 5/9 + 273.15

        elif from_unit == "Reamur":
            if to_unit == "Celsius":
                result = temperature * 5/4
            elif to_unit == "Fahrenheit":
                result = temperature * 9/4 + 32
            elif to_unit == "Kelvin":
                result = temperature * 5/4 + 273.15

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temperature - 273.15
            elif to_unit == "Fahrenheit":
                result = (temperature - 273.15) * 9/5 + 32
            elif to_unit == "Reamur":
                result = (temperature - 273.15) * 4/5

        result_label.config(text=f"{result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Masukkan suhu dalam angka")

# Membuat GUI
app = tk.Tk()
app.title("Aplikasi Konversi Suhu")
app.geometry("500x400")
app.configure(bg="#333")

# Judul program
title_label = tk.Label(app, text="Aplikasi Konversi Suhu", font=("Helvetica", 16, "bold"), bg="#333", fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky=tk.W+tk.E)

# Label nama pembuat program
name_label = tk.Label(app, text="Muhammad Faiz", font=("Helvetica", 12), bg="#333", fg="white")
name_label.grid(row=1, column=0, columnspan=3, pady=5, sticky=tk.W+tk.E)

# Label kelas pembuat program
class_label = tk.Label(app, text="TI22D", font=("Helvetica", 12), bg="#333", fg="white")
class_label.grid(row=2, column=0, columnspan=3, pady=5, sticky=tk.W+tk.E)

# Label NIM pembuat program
nim_label = tk.Label(app, text="220511139", font=("Helvetica", 12), bg="#333", fg="white")
nim_label.grid(row=3, column=0, columnspan=3, pady=5, sticky=tk.W+tk.E)

# Label dan Entry untuk Suhu Awal
from_label = tk.Label(app, text="Suhu Awal:", font=("Helvetica", 12), bg="#333", fg="white")
from_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
entry = tk.Entry(app, font=("Helvetica", 12))
entry.grid(row=4, column=1, padx=10, pady=10)

# Pilihan unit suhu awal
from_var = tk.StringVar()
from_var.set("Celsius")
from_unit_menu = tk.OptionMenu(app, from_var, "Celsius", "Fahrenheit", "Reamur", "Kelvin")
from_unit_menu.grid(row=4, column=2, padx=10, pady=10)

# Label dan Entry untuk Suhu Hasil
to_label = tk.Label(app, text="Konversi ke:", font=("Helvetica", 12), bg="#333", fg="white")
to_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

# Pilihan unit suhu hasil
to_var = tk.StringVar()
to_var.set("Fahrenheit")
to_unit_menu = tk.OptionMenu(app, to_var, "Celsius", "Fahrenheit", "Reamur", "Kelvin")
to_unit_menu.grid(row=5, column=1, padx=10, pady=10)

# Tombol untuk konversi
convert_button = tk.Button(app, text="Konversi", command=convert_temperature, font=("Helvetica", 12), bg="#4CAF50", fg="white")
convert_button.grid(row=6, column=0, columnspan=3, pady=10)

# Label untuk menampilkan hasil konversi
result_label = tk.Label(app, text="", font=("Helvetica", 12), bg="#333", fg="white")
result_label.grid(row=7, column=0, columnspan=3, pady=10)

# Menjalankan GUI
app.mainloop()
