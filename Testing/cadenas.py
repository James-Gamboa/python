# Archivo: cadenas.py
#  5. Crear una función llamada `es_palindromo(palabra)` que retorne `True` si la
# palabra es un palíndromo y `False` en caso contrario. Ignorar mayúsculas y
# espacios.
#  6. Crear una función llamada `contar_vocales(texto)` que cuente y retorne el
# número de vocales en una cadena de texto.

def es_palindromo(palabra):
    palabra_limpia = palabra.replace(" ", "").lower()
    return palabra_limpia == palabra_limpia[::-1]


def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador
