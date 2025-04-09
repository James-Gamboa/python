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