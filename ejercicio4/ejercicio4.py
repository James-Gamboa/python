# Ejercicio 4
# Escribe un programa en Python que cuente cuántas vocales hay en una frase ingresada por el usuario.

list_vowels = input("ingrese una frase: ")
vowels = ["a", "e", "i", "o", "u"]

for i in list_vowels:
    if i in vowels:
        print(i)
