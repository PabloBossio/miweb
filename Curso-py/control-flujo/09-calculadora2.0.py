print("Bienvenido a calculadora:")
print("Si desea salir ingrese salir.")
print("Las operaciones son: suma, resta, multi, div, pot.")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el otro número:")
    if n2.lower() == "salir":
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
    elif op.lower() == "pot":
        resultado **= n2
    else:
        print("Operación no valida.")
        break

    print(f"El resultado es: {resultado}")
