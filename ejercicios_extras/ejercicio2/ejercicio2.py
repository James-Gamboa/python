print("Bienvenido al Conversor de Unidades")
while True:
    print("\nMenú:")
    print("1. Metros a kilómetros")
    print("2. Gramos a kilogramos")
    print("3. Centígrados a Fahrenheit")
    print("4. Salir")
    choice = input("Elige una opción (1-4): ")
    if choice == "1":
        meters = float(input("Ingresa la cantidad en metros: "))
        km = meters / 1000
        print(meters, "metros son", km, "kilómetros.")
    elif choice == "2":
        grams = float(input("Ingresa la cantidad en gramos: "))
        kg = grams / 1000
        print(grams, "gramos son", kg, "kilogramos.")
    elif choice == "3":
        celsius = float(input("Ingresa la temperatura en °C: "))
        fahrenheit = (celsius * 9/5) + 32
        print(celsius, "°C son", fahrenheit, "°F.")
    elif choice == "4":
        print("Gracias por usar el conversor. ¡Adiós!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")