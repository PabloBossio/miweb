# hacer un programa que tome una lista con valores repetidos, y lograr que los elimine.
my_list = [1, 2, 4, 3, 4, 1, 5, 2, 5]
list2 = []

for i in my_list:
    if i not in list2:
        list2.append(i)

list2.sort()

print("Esta es la lista original:", my_list)
print("Esta es la lista sin repeticiones:", list2)
