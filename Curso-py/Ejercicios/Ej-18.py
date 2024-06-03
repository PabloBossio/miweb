# Triángulos y el Teorema de Pitágoras
# funcíon que dictamina si puede ser un triangulo.
def is_a_triangle(a, b, c): 
    return a + b > c or a + c > b or b + c > b

def right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > c and a > b:
        return a ** 2 == b ** 2 + c ** 2
    else: 
        return b ** 2 == a ** 2 + b ** 2

print(right_triangle(5, 3, 4))
print(right_triangle(3, 5, 4))
print(right_triangle(4, 3, 5))
print(right_triangle(3, 1, 4))
 