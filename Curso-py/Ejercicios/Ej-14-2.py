# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
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


def day_of_year(year, month, day):
    dia = 0
    for m in range(1, month):
        d = days_in_month(year, m)
        if d == None:
            return None
        dia += d
    if day >= 1 and day <= d:
        return dia + day
    else:
        return None


print(day_of_year(1986, 5, 23))
