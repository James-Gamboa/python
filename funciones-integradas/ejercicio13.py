# ✅ 13. Lista única y ordenada
# Dada una lista con elementos repetidos como [5, 3, 5, 2, 3, 1], crea una nueva lista con elementos
# únicos y ordenados.

def list_unique_and_sorted(list):
    return sorted(set(list))


numbers = [5, 3, 5, 2, 3, 1]

print(list_unique_and_sorted(numbers))
