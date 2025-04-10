# ✅ 12. Redondear una lista de decimales con map()
# Usa map() para redondear los números de una lista como [4.3, 5.7, 8.2].

def list_round(num):
    return round(num, 1)


numbers = [4.38, 5.76, 8.21]

rounded_numbers = list(map(list_round, numbers))
print(rounded_numbers)
