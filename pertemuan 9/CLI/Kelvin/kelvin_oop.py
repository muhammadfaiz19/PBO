class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_reamur(self):
        val = 4/5 * (self.suhu - 273)
        return val
    
    def get_fahrenheit(self):
        val = 9/5 * (self.suhu - 273) + 32
        return val
    
    def get_celcius(self):
        val = self.suhu - 273
        return val
    
suhu = input ("Masukan suhu dalam Kelvin : ")
C = Kelvin(float(suhu))
val = C.get_kelvin()

R = C.get_fahrenheit()
F = C.get_reamur()
C = C.get_celcius()

print ( str(val) + " Kelvin, sama dengan : ")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
print(str(C) + " Celcius")