def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b if b != 0 else '[!] Error: división por cero'

opc = 0
while opc != 5:

    print("\n===== Bienvenido a la Calculadora de Operaciones Básicas =====\n")


    a = int(input("Ingresa tu primer número: "))
    b = int(input("Ingresa tu segundo número: "))

    print("\n[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] División")
    print("[5] Salir")

    opc = int(input("Ingresa una opción: "))

    if opc == 1:
        print(suma(a,b))
    elif opc == 2:
        print(resta(a,b))
    elif opc == 3:
        print(multiplicacion(a,b))
    elif opc == 4:
        print(division(a,b))
    elif opc == 5:
        print("[+] Hasta Pronto")
        break
    else:
        print("[!] Opción no válida")

    
