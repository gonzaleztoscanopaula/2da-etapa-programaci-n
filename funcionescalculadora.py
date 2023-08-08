import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No es posible dividir entre 0")
    return a / b

def potenciacion(a, b):
    return a ** b

def radicacion(a, b):
    if a < 0 or b <= 0:
        raise ValueError("La radicación requiere un radicando no negativo y un índice positivo")
    return a ** (1 / b)

def coseno(angulo):
    return math.cos(math.radians(angulo))

def calculadora():
    print("Calculadora")
    while True:
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potenciación")
        print("6. Radicación")
        print("7. Coseno")
        print("8. Salir")
        
        operacion = input("Seleccione una operación (1/2/3/4/5/6/7/8): ")
        
        if operacion == "8":
            print("Saliendo de la calculadora")
            break
        
        if operacion in ("1", "2", "3", "4", "5", "6"):
            try:
                num1 = float(input("Ingrese el primer número: "))
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
                continue
        
        if operacion in ("1", "2", "3", "4", "5", "6"):
            try:
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
                continue
        
        if operacion == "1":
            resultado = suma(num1, num2)
        elif operacion == "2":
            resultado = resta(num1, num2)
        elif operacion == "3":
            resultado = multiplicacion(num1, num2)
        elif operacion == "4":
            try:
                resultado = division(num1, num2)
            except ValueError as e:
                print("Error:", e)
                continue
        elif operacion == "5":
            resultado = potenciacion(num1, num2)
        elif operacion == "6":
            try:
                resultado = radicacion(num1, num2)
            except ValueError as e:
                print("Error:", e)
                continue
        elif operacion == "7":
            try:
                angulo = float(input("Ingrese el valor del ángulo en grados: "))
                resultado = coseno(angulo)
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
                continue
        else:
            print("Operación no válida")
            continue
        
        print("Resultado:", resultado)

calculadora()
