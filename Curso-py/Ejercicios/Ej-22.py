# Si, existe algo de riesgo. Si no se considera una condición que detenga las invocaciones recursivas, el programa puede entrar en un bucle infinito. Se debe ser cuidadoso.
# El factorial también tiene un lado recursivo. Observa:
def factorial(n):
    if n < 1:
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

for i in range(1, 11):
    print(f"El factorial de {i} es: {factorial(i)}")
