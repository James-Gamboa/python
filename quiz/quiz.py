# Tu programa debe cumplir con las siguientes funcionalidades:
# 1. Interacción con el Usuario:
# o Solicita al usuario que ingrese la clave (key) del diccionario cuyo valor desea
# modificar.
# o Si la clave existe, permite al usuario ingresar un nuevo valor y actualiza dicha
# entrada en el diccionario.
# 2. Visualización del Estado Actual:
# o Una vez realizada la modificación, muestra en consola el diccionario actualizado,
# reflejando los cambios realizados.

# 3. Eliminación de Elementos:
# o Solicita al usuario que indique una clave a eliminar del diccionario.
# o Si la clave existe, elimínala y muestra el diccionario final luego de la eliminación.
# o En caso de que la clave no exista, informa al usuario que no se encontró la clave y
# muestra el diccionario sin cambios.

# 4. Robustez:
# o Asegúrate de manejar correctamente posibles errores, como claves inexistentes o
# entradas vacías.
# o El programa debe ser claro, intuitivo y fácil de usar, mostrando mensajes
# informativos en cada paso del proceso.

datos = {
  "producto": "Zapatillas Air Max",
  "talla": 42,
  "color": "rojo",
  "stock": 20
}

while True:
  print("1. Ingrese la Clave:")
  print("2. Visualización del Estado Actual")
  print("3. Eliminación de Elementos")
  print("4. Salir")
  opcion = input("Seleccione una Opcion: ")
  
  if opcion == "1":
    key = input("Ingrese la Clave: ")
    if key == "":
      print("La Clave no puede estar Vacia")
    new_value = input("Ingrese el Nuevo Valor: ")
    if new_value == "":
      print("El Nuevo Valor no puede estar Vacio")
    datos[key] = new_value
  elif opcion == "2":
    print("Estado actual de los datos:")
    print(datos)
  elif opcion == "3":
    key = input("Ingrese la clave que desea eliminar: ")
    if key in datos:
      del datos[key]
      print(datos)
  elif opcion == "4":
    print("Saliendo del Programa")  
    break
  
  # Menú interactivo:
# Crea un programa que muestre un menú con opciones.
# El usuario debe seleccionar una opción del menú, y el programa ejecutará una acción según la opción
# elegida. Si el usuario elige "Salir", el programa debe finalizar.
# Pista: Usa un while con una condición que se mantenga verdadera mientras el usuario no seleccione "Salir".
# Implementa opciones como "Mostrar mensaje", “Mostrar nombres", y "Salir".

print ("Bienvenido al Menú interactivo")
while True:
  print ("1. Mostrar Mensaje")
  print ("2. Mostrar Nombres")
  print ("3. Salir")
  opcion = int (input ("Seleccione una opción: "))
  if opcion == 1:
    your_message = input ("Ingrese su Mensaje: ")
    print("Tu Mensaje es", your_message)
  elif opcion == 2:
    show_name = input ("Ingrese el Nombre: ")
    print("Tu Nombre es", show_name)
  elif opcion == 3:
    print ("Saliendo del Menú interactivo ")
    break