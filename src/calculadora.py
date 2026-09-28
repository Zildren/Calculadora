def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    print("Calculadora")
    try:
        a = float(input("Primer número: "))
        op = input("Operación (+, -, *, /): ")
        b = float(input("Segundo número: "))
    except ValueError:
        print("Entrada no válida: escribe un número.")
        return

    operaciones = {
        "+": suma,
        "-": resta,
        "*": multiplicacion,
        "/": division,
    }

    if op not in operaciones:
        print("Operación no válida.")
        return

    try:
        print("Resultado:", operaciones[op](a, b))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()