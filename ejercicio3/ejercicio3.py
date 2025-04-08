# Ejercicio 3

# Escribe un programa que solicite al usuario una lista de números y luego cuente cuántos de esos números
# son pares y cuántos son impares.
# • Pide al usuario que ingrese una lista de números separados por comas.
# • Convierte la entrada en una lista de enteros.
# • Recorre la lista y cuenta cuántos números son pares y cuántos son impares.
# • Muestra el resultado al usuario.

list_numbers = input("Ingrese una lista de números separados por comas: ")
list_numbers = [int(number) for number in list_numbers.split(",")]

for i in list_numbers:
    if i % 2 == 0:
        print("El numero", i, "es par")
    elif i % 2 != 0:
        print("El numero", i, "es impar")
