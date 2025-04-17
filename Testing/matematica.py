# Archivo: matematica.py
# 1. Crear una función llamada `es_primo(n)` que devuelva `True` si un número es primo y
# `False` si no lo es.
# 2. Crear una función `factorial(n)` que calcule el factorial de un número. Debe lanzar una
# excepción si el número es negativo.
# 3. Crear una función `fibonacci(n)` que devuelva una lista con los primeros `n` términos de
# la serie de Fibonacci.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        raise ValueError("Número negativo")
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado


def fibonacci(n):
    resultado = []
    a, b = 0, 1
    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b
    return resultado
