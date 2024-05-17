# Metodo de ordenamiento burbuja
my_list = []
swapped = True
num = int(input("Cuantos elementos desea ordenar? "))

for i in range(num):
    val = float(input("Ingrese un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(
    f"""\nLista ordenada:
{my_list}
""")
