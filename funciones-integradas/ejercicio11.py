# ✅ 11. Convertir Celsius a Fahrenheit con map()
# Dada una lista de temperaturas en grados Celsius, conviértelas a Fahrenheit usando la fórmula:
# F = C * 9/5 + 32

def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


celsius_temperatures = [0, 10, 20, 30, 40]
fahrenheit_temperatures = list(
    map(convert_to_fahrenheit, celsius_temperatures))
print(fahrenheit_temperatures)
