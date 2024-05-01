numeros = (1, 2, 3) + (4, 5, 6)  # las tuplas son listas, no modificables.
print(numeros)
# otra forma de crear tuplas.
punto = tuple([1, 2])
print(punto)

# forma para crear nuevas tuplas, desde otra ya existente.
menosNumeros = numeros[1::2]
print(menosNumeros)

for n in numeros:
    print(n)

# forma de modificar tuplas (creando nuevas variable).
listaNumeros = list(numeros)
listaNumeros[0] = "chanchito feliz"
print(listaNumeros)
