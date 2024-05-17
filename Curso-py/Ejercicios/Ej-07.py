# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.
# Por cierto, eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?)

beatles = []

beatles.append("Jonh Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Estos son algunos de los Beatles:", beatles)

for i in range(4, 6):
    beatles.append(input("ingrese los nombres de los beatles faltantes: "))

print("Esta son los Beatles originales:", beatles)

del beatles[3]
del beatles[3]
print(f"Así quedaron los Beatles despues de sus primeros cambios: {beatles}")

beatles.insert(0, "Ringo Starr")
print(f"Estos son los Beatles conocidos por todos: {beatles}")
