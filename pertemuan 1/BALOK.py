"""
Muhammad Faiz
220511139
TI22D
Tugas Pertemuan 1 - PBO
"""

#Balok
print("Menghitung luas dan volume balok")

#Variable
panjang = float(input("masukan panjang : "))
lebar = float(input("masukan lebar : "))
tinggi = float(input("masukan tinggi : "))

#Rumus
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
volume = panjang * lebar * tinggi

#Output
print("jumlah dari sisi : ", luas)
print("volume dari kubus : ", volume)