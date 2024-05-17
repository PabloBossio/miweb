# Programa que cuenta la cantidad de numeros pares e impares,
# ingresados por el usuario.

impar = 0
par = 0
# Pedimos que el usuario ingrese un número.
number = input("Ingrese un número o el 0 si quiere salir. ")
number = int(number)
# inciamos el bucle while simpre que el usuario ingrese un número != a 0.
while number != 0:
    # Le damos una instrucción a while para que sepa que numero es impar.
    if number % 2 == 1:
        impar += 1
    else:
        par += 1

    number = input("Ingrese un número o el 0 si quiere salir.")
    number = int(number)

print("La cantidad de números pares son:", par)
print(f"La cantidad de números impares son: {impar}")
