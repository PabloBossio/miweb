# lista1 = [1, 2, 3, 4]
# print(1, 2, 3, 4)
# *operador de desempaquetamiento.
# print(*lista)

# lista2 = [5, 6]
# combinar listas, con el operado de desmpaquetamiento.
# combinadas = [*lista1, *lista2]

# cuando combinamos las listas, se pueden agregar valores.
# combinadas = ["hola", *lista1, "mundo", *lista2, "Pablo"]

# print(combinadas)

# uso del operador, en diccionarios.

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

# el operador, toma lee los valores desde la derecha, por ende cuando un valor ya esta asginado en un diccionario anterior se toma el de este.
# nuevoPunto = {**punto1, **punto2}
# print(nuevoPunto)

# como antes en el caso de los diccionarios, tambien podemos agregar valores por medio del operador.

nuevoPunto = {**punto1, "z": "hola", **punto2, "a": "mundo"}
print(nuevoPunto)
