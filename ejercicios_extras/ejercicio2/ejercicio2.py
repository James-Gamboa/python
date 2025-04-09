# Ejercicio 2
# La ciencia, la ingeniería y la vida cotidiana están llenas de conversiones de unidades.
# Desde calcular cuánto pesa un objeto en kilogramos hasta transformar distancias para un
# viaje, las conversiones son herramientas fundamentales que usamos sin darnos cuenta.
# En este ejercicio, te proponemos construir tu propio conversor de unidades. Será un
# pequeño programa interactivo donde el usuario podrá elegir qué tipo de conversión desea
# realizar y luego ingresar el valor que quiere convertir. El programa se encargará del resto y
# mostrará el resultado.
# Objetivos del ejercicio
#  Crear un menú interactivo para el usuario.
#  Recibir entradas numéricas del usuario.
#  Realizar conversiones matemáticas simples.
#  Repetir el proceso hasta que el usuario decida salir.
# Ejemplos
# 1. Metros a kilómetros
# Ejemplo: si el usuario ingresa 1200 metros, el resultado será 1.2 kilómetros.
# 2. Gramos a kilogramos
# Ejemplo: si el usuario ingresa 5000 gramos, el resultado será 5.0 kilogramos.
# 3. Centígrados a Fahrenheit
# Ejemplo: si el usuario ingresa 0 °C, el resultado será 32 °F.
# 4. Salir
# El programa finalizará amablemente cuando el usuario seleccione esta opción.

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