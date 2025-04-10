# ✅ 1. Filtrar los números pares de una lista usando filter()
# Dada una lista de números, utiliza filter() para obtener una nueva lista que contenga únicamente los
# números pares.

def filter_even_numbers(numbers):
    return numbers % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(filter_even_numbers, numbers)

print(list(even_numbers))
