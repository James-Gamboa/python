# Ejercicio

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