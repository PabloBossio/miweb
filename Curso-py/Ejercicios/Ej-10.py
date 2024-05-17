# hacer un programa que nos devuelva una lista sin numeros repetidos.

# creamos una lista vacia, para ingresarle los valores que usuario desee.
list1 = []
num = int(input("Cuantos valores quiere ingresar en la lista: "))
# creamos una lista vacía para poder copiar los datos que no esten repetidos de list1.
list_SR = []

# creamos un bucle for, para ingresar a list1 los datos que el usuario desee.
for i in range(num):
    val = int(input(
        "Ingrese los valor que quiere agregar a la lista: \n recuerde ingresar algunos valores iguales."))
    list1.append(val)

# creamos un bucle for, para poder copiar los datos no repetidos de list1 en list_SR.
for u in list1:
    if u not in list_SR:  # indicamos que si uno de los elementos de list1 no se encuentra en list_SR sea agregado al final de esta ultima.
        list_SR.append(u)

list_SR.sort()  # hacemos que list_SR este ordenada de menor a mayor.
print("Esta es la lista sin repeticiones:", list_SR)
