# Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los diccionarios pueden trabajar juntos.
# Imaginemos el siguiente problema:
# necesitas un programa para calcular los promedios de tus alumnos;
# el programa pide el nombre del alumno seguido de su calificación;
# los nombres son ingresados en cualquier orden;
# el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso Fundamentos de Python)
# una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
#inicializamos un diccionario vació.
school_class = {}

while True:
    name = input("ingrese el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingrese la nota del alumno (1/10): " ))
    if score not in range(1, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
            
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1

    print(name, ";", adding / counter)
