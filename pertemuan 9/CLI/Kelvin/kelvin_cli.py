print("Konversi Suhu Kelvin")
def get_reamur(suhu):
    R = 4/5 * (float (suhu) - 273) 
    return R

def get_fahrenheit(suhu):
    F = 9/5 * (float(suhu) - 273) + 32
    return F

def get_celcius(suhu):
    K = float(suhu) - 273
    return K

# Entry
suhu = input("Masukan suhu dalam Kelvin : ")

# Rumus
R = get_reamur(suhu)
F = get_fahrenheit(suhu)
C = get_celcius(suhu)

# Output
print(suhu + " Kelvin sama dengan")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
print(str(C) + " Celcius")