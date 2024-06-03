# Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los diccionarios pueden trabajar juntos.
# Imaginemos el siguiente problema:
# necesitas un programa para calcular los promedios de tus alumnos;
# el programa pide el nombre del alumno seguido de su calificación;
# los nombres son ingresados en cualquier orden;
# el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso Fundamentos de Python)
# una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
#inicializamos un diccionario vació. 
school_class = {}
# iniciamos un bucle infinito para poder recolctar datos del usuario.
while True:
    name = input("Ingrese el nombre del alumno: ")
    # si el usuario no ingresa un nombre salimos del bucle.
    if name == '':
        break
    
    score = int(input('ingrese la calificacion del estudiante (0/10) : '))
    # si la nota esta fuera del rango, salimos del bucle. 
    if score not in range(1, 11):
        break   
    # si el estudiante ya esta en el diccionario, sumamos la nueva calificacion a la ya existente.
    if name in school_class:
        school_class[name] += (score,)
    # si el estudiante no esta en el diccionario, lo añadimos junto con la calificación.
    else:
        school_class[name] = (score,)
# iteramos sobre los estudiantes del diccionario, oredenandolos alfabeticamente.
for name in sorted(school_class.keys()):
    # inicializamos contadores para sumar las calificaciones, y contar cada una de ellas.
    adding = 0
    counter = 0
    # iteramos sobre las calificaciones del alumno actual.
    for score in school_class[name]:
        adding += score # sumamos cada calificacion a la variable adding. 
        counter += 1 # incrementamos el contador de calificaciones.
    # Imprimimos el nombre del estudiante, y su calificacion promedio.
    print(name, ":", adding / counter)

