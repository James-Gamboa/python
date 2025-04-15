# Ejercicio (POO) Opción 1

# Cifrado de César
# Cuentan los antiguos escritos romanos que el emperador
# Julio César utilizaba este tipo de encriptación para cifrar
# sus mensajes militares y que sus enemigos no pudieran
# leerlos si capturaban al mensajero.
# Roma, con una gran mayoría de población analfabeta,
# este tipo de codificación era bastante segura. Incluso
# podía pasar por un mensaje escrito en lengua extranjera.
# Ejercicio (POO) Opción 1
# ¿Cómo funciona el cifrado de César?
# Clave de desplazamiento: El cifrado de César se basa en un número llamado "clave" o "desplazamiento". Este
# número indica cuántas posiciones hacia adelante se debe mover cada letra en el alfabeto. Por ejemplo,
# Si el desplazamiento es de 1, la letra "A" se convierte en “B“.
# Si el desplazamiento es de 1 la letra “Z" se convierte en “A",
# Si el desplazamiento es de 1, la letra “C" se convierte en “D",
# HOLA con un desplazamiento de 1 su cifrado es IPMBclass Juego:

# Ejercicio (POO) Opción 2
# Método de ordenamiento Bubble Sort
# Funcionamiento
# Comparación de elementos: El algoritmo comienza desde el primer elemento de la lista y compara el elemento
# actual con el siguiente.
# Intercambio: Si el elemento actual es mayor que el siguiente, se intercambian sus posiciones.
# Repetición: Este proceso se repite para cada par de elementos adyacentes en la lista. Al final de la primera pasada,
# el elemento más grande se "burbujea" hacia la última posición.

# Ejercicio (POO) Opción 2
# Método de ordenamiento Bubble Sort

class Juego:
    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido, {self.nombre_jugador}!")
        print("Selecciona el juego que deseas jugar:")
        print("1. Cifrado César")
        print("2. Ordenamiento Bubble Sort")
        opcion = input("Elige una opción (1 o 2): ")

        if opcion == "1":
            self.jugar_cifrado_cesar()
        elif opcion == "2":
            self.jugar_bubble_sort()
        else:
            print("Opción inválida. Volviendo al menú principal.")

    def jugar_cifrado_cesar(self):
        mensaje = input("\nIngresa un mensaje para cifrar: ")
        resultado = ""

        for letra in mensaje:
            if letra.isalpha():
                base = ord("A") if letra.isupper() else ord("a")
                nueva = chr((ord(letra) - base + 3) % 26 + base)
                resultado += nueva
            else:
                resultado += letra

        print(f"\nMensaje original: {mensaje}")
        print(f"Mensaje cifrado (desplazamiento 3): {resultado}")
        print("¡Juego de Cifrado César terminado!\n")

    def jugar_bubble_sort(self):
        try:
            entrada = input(
                "\nIngresa números separados por coma (ej: 5,3,8,1): ")
            numeros = list(map(int, entrada.split(",")))
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar solo números.")
            return

        for i in range(len(numeros)):
            for j in range(len(numeros) - 1 - i):
                if numeros[j] > numeros[j + 1]:
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

        print(f"Lista ordenada: {numeros}")
        print("¡Juego de Bubble Sort terminado!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")
