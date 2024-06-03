# Calcular el IMC y convertir unidades del Sistema Inglés al Sistema Métrico.
#definimos una funcion que convierte de pies y pulgadas a metros
def ft_inch_to_m(ft, inch = 0.0):
    # un pie equivale a 0.3048 metros y una pulgada a 0.0254 metros.
    return ft * 0.3048 + inch * 0.0254
# definimos una funcion que convierte de libras a kilos.
def lb_to_kg(lb):
    # una libra equivale a 0.4535923 kilos.
    return lb * 0.4535923
# definimos una funcion que calcule el IMC para la altura y peso, calculados con las demas funciones. 
def bmi(weight, height):
    # Comprobamos que la altura y peso sean datos razonables.
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        # si los datos de cualquiera de estas no son razonables, se returna None.
        return None
    # si los datos son razonables, se hace el calculo de IMC.
    return weight / height ** 2

print(bmi(weight= lb_to_kg(176), height= ft_inch_to_m(5, 7))) 