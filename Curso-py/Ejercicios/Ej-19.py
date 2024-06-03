# Evaluando el área de un triángulo

def is_a_triangle(a, b, c):
    return a + b > c or a + c > b or b + c > a

def heron(a, b, c):
    h = (a + b + c) / 2
    return (h * (h - a ) * (h - b) * (h - c)) ** 0.5

def area(a , b, c):
    if not is_a_triangle:
        return None
    return heron(a, b ,c)

print(area(1., 1., 2. ** .5))