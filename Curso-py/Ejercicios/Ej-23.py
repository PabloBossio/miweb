# La serie de Fibonacci es un claro ejemplo de recursividad. Ya te dijimos que:
# Fibi = Fibi-1 + Fibi-2
# El número i se refiere al número i-1, y así sucesivamente hasta llegar a los primeros dos.
# ¿Puede ser empleado en el código? Por supuesto que puede. Puede hacer el código más corto y claro.
# La segunda versión de la función fib() hace uso directo de la recursividad
 
def fib(n):
    if n < 1:
        return False
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, 11):
    print(f"Para {i}, Fibonacci = {fib(i)}")
    