# La serie de Fibonacci es un claro ejemplo de recursividad. Ya te dijimos que:
# Fibi = Fibi-1 + Fibi-2
# El número i se refiere al número i-1, y así sucesivamente hasta llegar a los primeros dos.
# ¿Puede ser empleado en el código? Por supuesto que puede. Puede hacer el código más corto y claro.
# La segunda versión de la función fib() hace uso directo de la recursividad
# funcion para calcular Fibonacci de x número.
def fib(n):
    # si el número es menor a 1, devolvemos flase, ya que no es un valor valido para Fibonacci  
    if n < 1:
        return False
    # si el número es menor a 3 (1 y 2), devolvemos 1, ya que los 2 primeros número en la serie Fibonacci son 1. 
    if n < 3:
        return 1
    # para otro caso, devolvemos la suma de los 2 anteriores números en la serie Fibonacci.
    return fib(n - 1) + fib(n - 2)

for i in range(1, 11):
    print(i, '=', fib(i))

