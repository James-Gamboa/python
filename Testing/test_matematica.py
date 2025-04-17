from matematica import es_primo, factorial, fibonacci
import pytest


def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(4) == False
    assert es_primo(17) == True
    assert es_primo(1) == False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6


def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
