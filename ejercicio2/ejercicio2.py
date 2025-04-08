# Ejercicio 2

# 1. Dada una edad clasifique esa edad si es nino, adolecente, adulto o adulto mayor
# 2. Se debe de crear una funcion para cada una de las validaciones
# 3. Imprimir al final el resultadode la validacion
# Condiciones
# edad < 13 = niño
# edad > = 13 && edad < 18 = Adolecente
# edad > = 18 && edad < 60 = Adulto
# edad > =60 = Adulto Mayor

list_age = [12, 13, 18, 24, 28, 30, 60, 61, 80, 100]
for i, age in enumerate(list_age):
    if age < 13:
        print("El usuario es un niño", age)
    elif age >= 13 and age < 18:
        print("El usuario es un adolescente", age)
    elif age >= 18 and age < 60:
        print("El usuario es un adulto", age)
    elif age >= 60:
        print("El usuario es un adulto mayor", age)
