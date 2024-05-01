# set significa grupo o conjunto.
primero = {1, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# print(primero | segundo) | es llamado unión y se usa para unir los valores de sets, y retornarlos sin que se repitan.
# print(primero & segundo) & & es llamado interseccion y se utiliza para devolver los valores que se encuentra repetidos en los sets.
# print(primero - segundo) - es llamado diferencia y se usa para eliminar los valores repetidos en los sets, del primero de estos.
# print(primero ^ segundo) ^ es llamado diferencia simetrica, y se utiliza como el anterior, pero devolviendo los valores de todos los sets.

# segundo[0] = 5 no se puede ingresar a los valores de los sets.

# podemos preguntar si es que existe un valor dentro de los sets.
if 5 in segundo:
    print("Si")
