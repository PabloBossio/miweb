# Escenario
# Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

# La figura ilustra la regla utilizada por los constructores:

# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

# Prueba tu código con los datos que hemos proporcionado.
# pedimos al usuario la cantidad de bloques disponibles para la piramide.
bloques_disponibles = int(
    input("Ingrese la cantidad de bloques disponibles: "))

# creamos variables en cero para poder usarlas en while y asignarles sus valores correspondients.
altura_piramide = 0
bloques_usados = 0

while bloques_usados < bloques_disponibles:  # iniciamos el while
    altura_piramide += 1
    # para poder sumar un piso a la piramide y sumar los bloques utilizados
    bloques_usados += altura_piramide

    # para poder salir del bucle cuando ya no queden bloques suficientes.
    if bloques_usados > bloques_disponibles:
        altura_piramide -= 1
        break

# mostramos los resultados.
print(f"""La altura alcanzada con esta cantidad de bloques es: {
      altura_piramide}""")
