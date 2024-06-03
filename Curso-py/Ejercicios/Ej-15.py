# Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.
# ¿Complicado? De ningúna manera. Por ejemplo, 8 no es un número primo, ya que puedes dividirlo entre 2 y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).
# Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el.
# Tu tarea es escribir una función que verifique si un número es primo o no.
# La función:
# se llama is_prime;
# toma un argumento (el valor a verificar)
# devuelve True si el argumento es un número primo, y False de lo contrario.
# Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y verifica el resto - si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo deberías detener el proceso.
# Si necesitas conocer la raíz cuadrada de cualquier valor, puedes utilizar el operador **. Recuerda: la raíz cuadrada de x es lo mismo que x0.5.
# Complementa el código en el editor.
# Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
def is_prime(n):
    # verificamos que el número sea mayor que 1, en caso contrario no es primo.
    if n <= 1:
        return False
    # verificamos que el número sea mayor que 3, en caso contrario y cumpliendo el anterior "if" son primos.
    if n <= 3:
        return True
    # verificamos si son divisibles por 2 y 3, si no lo son pueden ser primos.
    if n % 2 == 0 or n % 3 == 0:
        return False
    # inicilizamos una variable en 5. 
    i = 5
    # mientras el cuadrado de i sea menor o igual al número n.
    while i * i <=n:
        # verificamos si n es devisible por i o por (i+2).
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # incrementamos i en 6, para verificar otro posibles factores. 
        i += 6 
    # si no se encuentra ningún divisor, el número es primo.
    return True

for u in range(1, 20):
    if is_prime(u + 1):
        print(u + 1, end=" ")
print()
