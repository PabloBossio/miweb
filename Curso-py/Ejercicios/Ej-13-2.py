# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

def year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]

    if month == 2 and year_leap(year):
        res = 29

    return res


years = [1987, 1996, 2001, 2004, 2021]
months = [4, 5, 2, 2, 2]
resul = [30, 31, 28, 29, 28]

for i in range(len(years)):
    yr = years[i]
    mo = months[i]
    print(yr, mo, "->", end='')
    result = days_in_month(yr, mo)
    if result == resul[i]:
        print("OK")
    else:
        print("Fail")
