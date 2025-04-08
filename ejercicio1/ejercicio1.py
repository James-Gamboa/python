# Ejercicio 1

# 1. Cree una función de bienvenida para un usuario que se encargue de dar la bienvenida a un usuario X
# debe solicitar el nombre del usuario
nombre = input("Ingrese su nombre: ")
print("Bienvenido ", nombre)

# 2. Cree una funcion que se encargue de tomar dos notas y determine su promedio
nota = input("Ingrese la primera nota: ")
nota2 = input("Ingrese la segunda nota: ")
suma_promedio = int(nota + nota2) / 2
print("El promedio es: ", suma_promedio)

# 3. Cree una funcion que permita mostrar el resultado del promedio al usuario, se debe mostrar el nombre
# del usuario y el promedio
user_name = input("Ingrese su nombre: ")
note = input("Ingrese la primera nota: ")
note2 = input("Ingrese la segunda nota: ")
average_sum = int(nota + nota2) / 2
print("Hola", user_name, "su promedio es: ", average_sum)
