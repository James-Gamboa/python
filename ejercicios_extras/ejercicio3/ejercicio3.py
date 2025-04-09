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