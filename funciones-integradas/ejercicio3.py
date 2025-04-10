# ✅ 3. Convertir palabras en minúsculas a MAYÚSCULAS usando map()
# Dada una lista de palabras en minúsculas, usa map() para convertir todas las palabras a mayúsculas.

def convert_shift(word):
    return word.upper()


words = ["heredia", "alajuela", "cartago", "limon"]

print(list(map(convert_shift, words)))
