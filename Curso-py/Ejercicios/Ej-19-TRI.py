# Evaluando el área de un triángulo

def is_a_triangle(a, b, c):
    return a + b > c or b + c > a or c + a > b
# definimos una función para calcualar el areá de un triángulo con la formula de Herón. 
def heron(a, b, c):
    #calculamos el semiperímetro del triángulo.
    h = (a + b +c) / 2 
    # usamos la formula de Herón para el calculo del areá.
    return (h * (h - a) * (h - b) * (h - c)) ** 0.5
# definimos una función para el calculo del areá, verifincando si el triángulo es valido. 
def area_of_triangle(a, b , c):
    # si no lo es, devolvemos None.
    if not is_a_triangle(a, b, c):
        return None
    # si lo es ejecutamos la función heron.
    return heron(a, b, c)

print(area_of_triangle(1., 1., 2. ** .5))
