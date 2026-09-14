from Suma import sumar

op = -1

while op != 0:
    print("Menu:")
    print("1. Suma")
    print("0. Salir")
    op = int(input("Seleccione la opcion deseada: "))

    if op == 1:
        a = float(input("Digite el primer numero: "))
        b = float(input("Digite el segundo numero: "))
        print("Resultado:", sumar(a, b))
    elif op == 0:
        print("Adios broo")
    else:
        print("Opcion no valida")