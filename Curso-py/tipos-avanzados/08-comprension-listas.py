usuarios = [
    ["pulga", 5],
    ["chanchito", 4],
    ["Felipe", 1]
]

# nombres = [] forma de pedir que nos retorne uno de los valores de las listas.
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# map
# nombres = [usuario[0] for usuario in usuarios] forma de pedir que nos retorne uno de los valores en una sola linea, creando nueva lista.
# filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2] forma de pedir que nos retorne ciertos valores de la lista, filtrando la misma.

# forma de hacer los dos items anterioes en un solo paso.
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# uso de la funcion map.
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# uso de la funcion filter.
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
