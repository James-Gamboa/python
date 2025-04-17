import pytest
from operaciones import suma, resta, multiplicar, dividir


def test_suma():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0


def test_resta():
    assert resta(5, 3) == 2
    assert resta(3, 5) == -2


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6


def test_dividir():
    assert dividir(10, 2) == 5

    with pytest.raises(ValueError):
        dividir(5, 0)
