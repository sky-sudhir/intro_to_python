def celsius_to_fahernheit(c):
    return (c*(9/5))+32

def fahrenheit_to_kelvin(f):
    return ((f-32)/1.8)+273.15

def kelvin_to_celcius(k):
    return k-273.15

cToF=celsius_to_fahernheit(0)
fToK=fahrenheit_to_kelvin(32)
kToC=kelvin_to_celcius(300)

print(f"0 C = {cToF}F")
print(f"32 F  = {fToK}K")
print(f"300 K = {kToC}C")