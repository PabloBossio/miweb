# Calculadora en python
# Presentación del programa al usuario
print("Bienvenido a su calculadora en python.")
print("Si desea salir ingrese salir.")
print("Las operaciónes posibles son suma, resta, multi y div.")

resultado = ""

while True:  # Para tomar datos del usuario de forma fluida
    if not resultado:  # Para poder ingresar al if uso el comando not y anteriormente asignamos una variable sin valor.
        resultado = input("Ingrese el primer valor: ")
        # .lower() lo utilizo para que sin importar como el usuario ingrese los comandos, estos sean leidos por el porgrama.
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("Ingrese la operación que quiere realizar: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese el segundo valor: ")
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
        resultado //= n2
    else:
        print("La operación solicitada no es correcta.")
        break

    print(f"El resultado de su operacion es: {resultado}")
