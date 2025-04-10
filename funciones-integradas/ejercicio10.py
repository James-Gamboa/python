# ✅ 10. Ordenar tuplas por el segundo valor con sorted()
# Dada una lista de tuplas como [("Juan", 25), ("Ana", 20), ("Luis", 30)], ordénala por edad

def sort_by_age(tupla):
    return tupla[1]


tuplas = [("Juan", 25), ("Ana", 20), ("Luis", 30)]
sorted_tuplas = sorted(tuplas, key=sort_by_age)
print(sorted_tuplas)
