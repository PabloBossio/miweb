print("Bienvenido a tu calculadore de python:")
print("Para salir escribe salir.")
print("las operaciones son: suma, resta, multi y div.")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida.")
        break
    print(f"EL resultado es {resultado}")
