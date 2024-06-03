# La siguiente función a definir calcula factoriales. ¿Recuerdas cómo se calcula un factorial?

# 0! = 1 (¡Si!, es verdad)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 * ... * n-1 * n

# Se expresa con un signo de exclamación, y es igual al producto de todos los números naturales previos al argumento o número dado.

# Escribamos el código. Creemos una función con el nombre factorial_function.

def factorial_fuction(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for u in range(1, 11):
    print(u, factorial_fuction(u))
