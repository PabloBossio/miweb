# ¿Estás familiarizado con la serie Fibonacci?
# Son una secuencia de números enteros los cuales siguen una regla sencilla:
# el primer elemento de la secuencia es igual a uno (Fib1 = 1)
# el segundo elemento también es igual a uno (Fib2 = 1)
# cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
# Aquí están algunos de los primeros números en la serie Fibonacci:
# fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13
# ¿Que opinas acerca de implementarlo como una función?

def fibonacci(n):
    # validando casos falsos.
    if n < 1:
        return None
    # si el número es menor a 3 el resultado de fibonacci sera 1.
    if n < 3:
        return 1 
    
    #inicializamos los dos primeros elementos de fibonacci en 1.
    elem_1 = elem_2 = 1
    # inicializamos un variable suma en 0, para guardar el resultado.
    suma = 0
    # iteramos desde 3 hasta n incluyendolo, para calcular la secuencia.  
    for n in range(3, n + 1):
        # la variable suma = a la suma de los dos elementos.
        suma = elem_1 + elem_2
        # Actualizamos lo elmentos, (el 2do se convierte en el 1ro, y la suma en le 2do.) 
        elem_1, elem_2 = elem_2, suma
    return suma

# Prueba
for u in range(1, 11):
    print(u, "->", fibonacci(u))
