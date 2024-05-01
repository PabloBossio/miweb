numeros = [1, 5, 3, 18, 12, 70, 30]

# numeros.sort()  para ordenar numeros de menor a mayor en una lista.
# numeros.sort(reverse=True)  para ordenar de mayor a menor una lista de numeros.
# numeros2 = sorted(numeros) igualmente ordena los numeros en la lista, pero creando una nueva.
# numeros2 = sorted(numeros, reverse=True) # los ordena de mayor a menor, creando una nueva lista.
# print(numeros)
# print(numeros2)

usuarios = [               # forma de ordenar listas, con listas dentro.
    ["pulga", 5],
    ["chanchito", 4],
    ["Felipe", 1]
]

# usuarios.sort()
# print(usuarios)


# otra forma de ordenar listas con listas dentro.
# def ordena(elemento):
#     return elemento[1]

# forma más estetica de hacerlo, pero solo si se debe hacer una vez en todo el cogigo.
usuarios.sort(key=lambda el: el[1])
print(usuarios)
