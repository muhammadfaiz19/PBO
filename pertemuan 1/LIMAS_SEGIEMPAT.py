"""
Muhammad Faiz
220511139
TI22D
Tugas Pertemuan 1 - PBO
"""

#Limas Segiempat
print("menghitung luas dan volume limas segi empat")

#Variable
sisi = float(input("masukan jumlah sisi : "))
luasAlas = float(input("masukan luas alas : "))
tinggi = float(input("masukan tinggi : "))

#Rumus
luas = luasAlas + sisi
volume = 1/3 * luasAlas * tinggi

#Output
print("luas dari limas segitiga : ", luas)
print("volume dari limas segiempat : ", volume)