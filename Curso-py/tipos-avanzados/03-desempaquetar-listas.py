numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros # para llamar a distintos elementos de una lista, esteticamente.
# print(primero, segundo, tercero)

primero, segundo, *otros, penu, ultimo = numeros
# para llamar un valor de la lista, y mantener a los demas dentro de ella.
print(segundo, penu, otros)
