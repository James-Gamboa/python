# Ejercicio 1

# En este ejercicio vas a programar una versión digital de ese clásico juego mental. La
# computadora elegirá un número aleatorio entre 1 y 100, y tu misión será adivinarlo. Pero no
# estarás completamente a oscuras: después de cada intento, el programa te dirá si tu
# número es demasiado bajo o demasiado alto, ayudándote a acercarte poco a poco a la
# respuesta correcta.
# Consejos
#  Uso del módulo random para generar números aleatorios.
#  Entrada y salida de datos con input() y print().
#  Bucles while para repetir acciones hasta que se cumpla una condición.
#  Estructuras condicionales if para comparar valores y tomar decisiones.
#  Contadores para saber cuántos intentos se han realizado.
# Escribir un programa que:
# 1. Elija un número aleatorio entre 1 y 100.
# 2. Le pida al usuario que intente adivinarlo.
# 3. Después de cada intento, indique si el número es más alto o más bajo.

import random

secret_number = random.randint(1,100)
attempts = 0
print("Adivina el número que estoy pensando (entre 1 y 100).")
while True:
    guess_input = input("Ingresa tu adivinanza: ")
    try:
        guess = int(guess_input)
    except:
        print("Por favor, ingresa un número válido.")
        continue
    attempts = attempts + 1
    if guess < secret_number:
        print("Demasiado bajo.")
    elif guess > secret_number:
        print("Demasiado alto.")
    else:
        print("¡Correcto! Adivinaste el número en", attempts, "intentos.")
        break