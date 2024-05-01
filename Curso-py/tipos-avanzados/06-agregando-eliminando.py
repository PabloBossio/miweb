mascotas = [
    "wolfgang",
    "pelusa",
    "pulga",
    "Felipe",
    "pulga",
    "chanchito"
]
# para insertar en el indice indicado un nuevo valor.
mascotas.insert(1, "Melvin")
# para insertar al final de la lista un nuevo valor.
mascotas.append("chanchito feliz")
# para eliminar la primera ocurrencia de un valor en una lista,
# o el valor si este no se encuentra repetido.
mascotas.remove("pulga")
# para eliminar el ultimo valor de una lista.
mascotas.pop()
# para eliminar el valor indicado con el indice, en una lista.
mascotas.pop(1)
# otra forma de eliminar valores de un arreglo.
del mascotas[0]
# para limpiar completamente un arreglo.
mascotas.clear()
print(mascotas)
