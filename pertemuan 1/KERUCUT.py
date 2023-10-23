"""
Muhammad Faiz
220511139
TI22D
Tugas Pertemuan 1 - PBO
"""

#kerucut

import math

print("Menghitung luas dan volume kerucut")

#Variable
oi = 22/7
tinggi = float(input("masukan tinggi : "))
jari_jari = float(input("Masukkan jari-jari bola: "))
tambahan = math.sqrt((jari_jari**2)+(tinggi*tinggi))

#Rumus
luas = oi*jari_jari*(jari_jari+tambahan)
volume = 1/3*oi*(jari_jari**2)*tinggi

#Output
print("Luas permukaan bola adalah:", luas)
print("Volume bola adalah:", volume)