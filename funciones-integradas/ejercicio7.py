# ✅ 7. Filtrar palabras cortas con filter()
# Dada una lista de palabras, usa filter() para eliminar todas las que tengan menos de 5 letras.
def filter_short_words(word):
    return len(word) >= 5


words = {"elden ring", "sekiro", "bloodborne", "rust",
         "dayz", "metal gear solid", "age of empires"}

print(list(filter(filter_short_words, words)))
