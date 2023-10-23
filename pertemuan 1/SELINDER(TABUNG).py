"""
Muhammad Faiz
220511139
TI22D
Tugas Pertemuan 1 - PBO
"""

#Tabung
print("Menghitung luas dan volume tabung")

#Variable
oi = 22/7
jari_jari = float(input("masukan jari jari : "))
tinggi = float(input("masukan tinggi : "))

#Rumus
luas = 2*oi*jari_jari*(jari_jari+tinggi)
volume = oi*jari_jari*jari_jari*tinggi

#Output
print("luas permukaan tabung : ", luas)
print("volume tabung : ", volume)