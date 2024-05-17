# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
# Esta función determina si un año es bisiesto.
def year_leap(year):
    if year % 4 != 0:  # si un año no es divisible por 4, no lo es.
        return False
    elif year % 100 != 0:  # si un año es divisible por 4 pero no por 100, lo es.
        return True
    elif year % 400 != 0:  # si un año es divisible por 100 pero no por 400, no lo es.
        return False
    else:  # si un año es divisible por 400 es bisiesto.
        return True

# esta función devuelve la cantidad de dias en un mes dado.


def days_in_month(year, month):
    # si es antes de 1582 no es parte del calendario gregoriano.
    if year < 1582 or month < 1 or month > 12:
        # ademas el mes debe ir de 1 a 12.
        return None
    # se hace una lista con los dias de cada mes, (febrero suele tener 28).
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # se selecciona la cantidad de dias dependiendo el mes dado.
    res = days[month - 1]
    # si es febrero y el año es bisiesto febrero cuenta con 29 dias.
    if month == 2 and year_leap(year):
        res = 29
    return res

# esta función calcula el dia de año, dando como argumento un año, mes, y dia.


def day_of_year(year, month, day):
    days = 0
    # se itera atraves de los meses anteriores al mes dado.
    for m in range(1, month):
        d = days_in_month(year, m)
        if d == None:  # si algun mes no es valido se devulve None
            return None
        days += d
    # si el dia es valido para el mes dado, se suma a la cantidad de dias.
    d = days_in_month(year, month)
    if day >= 1 and day <= d:
        return days + day
    else:  # si no es valido se returna None
        return None


print(day_of_year(2000, 2, 18))
print(day_of_year(1972, 2, 1))
print(day_of_year(2010, 12, 18))
