# Ejercicio 3
# En el mundo real, los sistemas de gestión de inventario son herramientas
# fundamentales para cualquier negocio que maneje productos. Desde una tienda
# minorista hasta un almacén mayorista, un buen control de inventario asegura que se
# conozcan las cantidades disponibles de productos, sus precios y la facilidad para
# añadir o eliminar artículos.
# Vas a crear un sistema simple de gestión de inventario, que permitirá al usuario
# realizar diversas operaciones sobre un conjunto de productos. A través de un menú
# interactivo, el programa deberá ser capaz de mostrar el inventario actual, permitir la
# adición de nuevos productos, modificar las cantidades o precios de productos
# existentes, y eliminar productos cuando ya no sean necesarios.
# Objetivos del ejercicio
# El objetivo de este ejercicio es desarrollar un programa interactivo con las siguientes
# funcionalidades:
# 1. Ver el inventario actual
# El usuario podrá ver todos los productos registrados en el inventario, mostrando su
# nombre, cantidad y precio.
# 2. Agregar nuevos productos
# El usuario podrá agregar productos al inventario. Para cada producto, deberá
# ingresar su nombre, cantidad y precio.
# 3. Modificar la cantidad de un producto existente
# El usuario podrá modificar la cantidad de un producto específico. Esto es útil si se ha
# vendido más unidades o si se han recibido más productos en el inventario.
# 4. Eliminar productos
# El usuario podrá eliminar productos que ya no están disponibles o que han sido
# descontinuados.
# 5. Salir del sistema
# El programa debe finalizar cuando el usuario elija esta opción.

# Características del sistema
#  Productos: Cada producto tiene tres características clave:
# o Nombre: El nombre del producto.
# o Cantidad: La cantidad de unidades disponibles.
# o Precio: El precio de cada unidad del producto.
#  Inventario: El inventario se puede almacenar usando un diccionario donde las
# claves son los nombres de los productos y los valores son otros diccionarios que
# contienen la cantidad y el precio.
#  Interactividad: El programa debe ser interactivo, mostrando un menú con opciones
# claras para que el usuario pueda elegir lo que desea hacer (ver inventario, agregar,
# modificar, eliminar, salir).

inventory = {}
while True:
    print("\nMenú de Inventario:")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Modificar cantidad de un producto")
    print("4. Eliminar producto")
    print("5. Salir")
    option = input("Elige una opción (1-5): ")
    if option == "1":
        if len(inventory) == 0:
            print("El inventario está vacío.")
        else:
            for product in inventory:
                data = inventory[product]
                print("Producto:", product, "- Cantidad:", data["cantidad"], "- Precio:", data["precio"])
    elif option == "2":
        name = input("Nombre del producto: ")
        quantity = int(input("Cantidad: "))
        price = float(input("Precio: "))
        inventory[name] = {"cantidad": quantity, "precio": price}
        print("Producto agregado correctamente.")
    elif option == "3":
        name = input("Nombre del producto a modificar: ")
        if name in inventory:
            new_quantity = int(input("Nueva cantidad: "))
            inventory[name]["cantidad"] = new_quantity
            print("Cantidad actualizada.")
        else:
            print("El producto no existe.")
    elif option == "4":
        name = input("Nombre del producto a eliminar: ")
        if name in inventory:
            del inventory[name]
            print("Producto eliminado.")
        else:
            print("El producto no existe.")
    elif option == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")