# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

# Tu tarea es:

# escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
# escribir una línea de código que elimine el último elemento de la lista (Paso 2)
# # escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
# creamos la lista.
sombrero = [1, 2, 3, 4, 5]

print(f"Esta es la lista de nuestro sombrero: {sombrero}")
# pedimos el cambio del valor en el número del indice 2.
sombrero[2] = int(
    input("\nIngrese el número por el que quiere cambiar al valor del indice 2: "))
print(f"Así quedo nuestra nueva lista con el cambio del número: {sombrero}")

# eliminamos el ultimo elemento de la lista.
del sombrero[4]
print(f"\nAsí queda la lista luego de eliminar su ultimó elemento: {sombrero}")

print("\nEsta es la longitud que ha quedado con la lista modificada:", len(sombrero))
