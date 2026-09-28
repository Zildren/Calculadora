from src.calculadora import suma, resta, multiplicacion, division


def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 3) == 2


def test_multiplicacion():
    assert multiplicacion(4, 3) == 12

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

