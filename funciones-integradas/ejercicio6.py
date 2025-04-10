# ✅ 6. Obtener longitudes de palabras con map()
# Dada una lista de palabras, usa map() para obtener una lista con la longitud de cada palabra.

def length(word):
    return len(word)


words = ["elden ring", "sekiro", "bloodborne",
         "demon souls", "dark souls", "vampire survivors"]

print(list(map(length, words)))
