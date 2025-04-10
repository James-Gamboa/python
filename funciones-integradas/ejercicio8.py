# ✅ 8. Convertir una lista de strings a enteros con map()
# Convierte una lista como ["1", "2", "3"] a enteros usando map().

def convert_to_int(string):
    return int(string)


string = ["1", "2", "3"]

print(list(map(convert_to_int, string)))
