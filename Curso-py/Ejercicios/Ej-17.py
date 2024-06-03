# Calcular el IMC y convertir unidades del Sistema Inglés al Sistema Métrico.
def ft_inch_to_m(ft,inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def lib_to_kg(lb):
    return lb * 0.453592
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2

print(bmi( weight= lib_to_kg(120), height= ft_inch_to_m(6, 2)))
