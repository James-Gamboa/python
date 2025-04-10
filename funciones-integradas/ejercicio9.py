# ✅ 9. Filtrar números positivos con filter()
# Dada una lista de números (positivos y negativos), filtra solo los positivos.
def filter_positive_numbers(number):
    return number > 0


numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]

print(list(filter(filter_positive_numbers, numbers)))
