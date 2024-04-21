import math

n1 = input("Ingrese el primer número")
n2 = input("Ingrese el segundo número")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 // n2
pot1 = pow(n1, n2)
pot2 = pow(n2, n1)
raiz1 = math.sqrt(n1)
raiz2 = math.sqrt(n2)
mensaje = f"""
Los resultados de las operacione realizadas con los nuemros \"{n1}\" y \"{n2}\" son:
Suma de los números: {suma}
Resta de los números: {resta}
Multiplicación de los números: {multi}
División de los números: {div}
Potencia del 1er número, elevado al 2do: {pot1}
Potencia del 2do número, elevado al 1er: {pot2}
Raíz cuadrada del 1er número: {raiz1}
Raíz cuadrada del 2do número: {raiz2}
"""
print(mensaje)
