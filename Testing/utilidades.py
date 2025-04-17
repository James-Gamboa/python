# Archivo: utilidades.py
# 4. Crear una función `formatear_nombre(nombre)` que devuelva el nombre capitalizado.
# Ejemplo: "juan pérez" → "Juan Pérez".
# 5. Crear una función `es_correo_valido(correo)` que devuelva `True` si el correo tiene un
# formato correcto, por ejemplo: algo@algo.com.
# 6. Crear una función `contar_palabras(texto)` que devuelva cuántas palabras hay en un
# texto.
def formatear_nombre(nombre):
    return nombre.title()


def es_correo_valido(correo):
    return "@" in correo and "." in correo and correo.index("@") < correo.rindex(".")


def contar_palabras(texto):
    return len(texto.split())
