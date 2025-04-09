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

print ("Bienvenido al conversor de unidades")
while True:
  print ("1. Metros a kilómetros")
  print ("2. Gramos a kilogramos")
  print ("3. Centígrados a Fahrenheit")
  print ("4. Salir")
  opcion = int (input ("Seleccione una opción: "))
  if opcion == 1:
    metros = float (input ("Ingrese los metros: "))
    kilometros = metros / 1000
    print (metros, "metros son", kilometros, "kilómetros")
  elif opcion == 2:
    grams = float (input ("Ingrese los gramos: "))
    kilograms = grams / 1000
    print (grams,"gramos son" , kilograms, "kilogramos")
  elif opcion == 3:
    centigrados = float (input ("Ingrese los Centígrados:"))
    fahrenheit = (centigrados * 1.8) + 32
    print (centigrados , "Centígrados son" , fahrenheit, "Fahrenheit")
  elif opcion == 4:
    print ("Saliendo del Sistema de Conversion")
    break