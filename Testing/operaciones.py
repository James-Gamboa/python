# Archivo: operaciones.py
#  Crear una función llamada `suma(a, b)` que retorne la suma de dos números.
#  Crear una función llamada `resta(a, b)` que retorne la resta entre dos números.
#  Crear una función llamada `multiplicar(a, b)` que retorne la multiplicación de dos
# números.
#  Crear una función llamada `dividir(a, b)` que retorne la división de dos números.
# Debe lanzar un error `ValueError` si el divisor es cero( Esto lo debes
# investigar).


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
