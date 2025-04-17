from utilidades import formatear_nombre, es_correo_valido, contar_palabras


def test_formatear_nombre():
    assert formatear_nombre("juan pérez") == "Juan Pérez"
    assert formatear_nombre("ana maria") == "Ana Maria"


def test_es_correo_valido():
    assert es_correo_valido("correo@ejemplo.com") == True
    assert es_correo_valido("correo.com") == False
    assert es_correo_valido("correo@ejemplo") == False


def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("Esto es una prueba de palabras") == 6
    assert contar_palabras("") == 0
