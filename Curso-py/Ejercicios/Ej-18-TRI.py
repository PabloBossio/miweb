# Triángulos y el Teorema de Pitágoras
# función que dictamina si puede ser un triángulo.
def is_a_triangle(a, b, c):
    # si la suma de dos lados es mayor que el 3er lado, puede ser un triángulo.
    return a + b > c and b + c > a and a + c > b

# función para saber si un triángulo es rectángulo.
def right_triangle(a, b, c):
    # verifcamos si el triangulo es rectangulo.
    if not is_a_triangle(a, b, c):
        return False
    # determinamos que lado es el mayor, y verificamos la condición del teorema de Pitágoras.
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if a > c and a > b:
        return a ** 2 == b ** 2 + c ** 2 
    else:
        return b ** 2 == a ** 2 + c ** 2

print(right_triangle(5, 3, 4))
print(right_triangle(3, 5, 4))
print(right_triangle(4, 3, 5))
print(right_triangle(3, 1, 4)) 
