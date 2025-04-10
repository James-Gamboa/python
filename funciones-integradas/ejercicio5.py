# ✅ 5. Redondear los valores de un diccionario
# Crea un programa en Python que reciba un diccionario con valores decimales y devuelva un nuevo
# diccionario con los valores redondeados.

dates = {
    "date1": 4.8,
    "date2": 5.7,
    "date3": 8.8,
    "date4": 6.9,
    "date5": 9.6,
    "date6": 7.8,
    "date7": 3.8
}

rounded_dates = {key: round(value) for key, value in dates.items()}
print(rounded_dates)
