# ✅ 2. Triplicar cada número de una lista usando map()
# Dada una lista de números, usa map() para crear una nueva lista con cada número triplicado.

def triplicate(num):
    return num * 3


numbers = [1, 2, 3, 4, 5]
tripled_numbers = list(map(triplicate, numbers))
print(tripled_numbers)
