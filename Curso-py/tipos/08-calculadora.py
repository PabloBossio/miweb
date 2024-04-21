n1 = input("Ingrese primer numero")
n2 = input("Ingrese segundo numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Los resultados de las operaciones de los numeros {n1} y {n2} son:
Suma= {suma}
Resta= {resta}
Multiplicación= {multi}
División= {div}
"""
print(mensaje)
