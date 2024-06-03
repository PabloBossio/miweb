# Si, existe algo de riesgo. Si no se considera una condición que detenga las invocaciones recursivas, el programa puede entrar en un bucle infinito. Se debe ser cuidadoso.
# El factorial también tiene un lado recursivo. Observa:
# función para calcular el factorial de un número.
def factorial(n):
    # si el número es menor a 1, devolvemos None, ya que factorial no esta definido para estos casos 
    if n < 1:
        return None
    # si el número es menor a 2 (0 o 1), devolvemos 1, ya que este es el factorial por definición.
    if n < 2:
        return 1
    # Para otro caso, devlovemos n multiplicado por el factorial de n - 1, (recursiva). 
    return n * factorial(n - 1) 

for i in range(1, 11):
    print(i, '=', factorial(i))
