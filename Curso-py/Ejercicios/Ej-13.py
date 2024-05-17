# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
# funcion que registra si un año es bisiesto o no.
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# función que devuelve la cantidad de dias en un mes especifico en un año en particular.


def days_in_month(year, month):
    # verificacion de la validez del año y mes.
    if year < 1582 or month < 1 or month > 12:
        return None
    # lista con los dias de cada mes (no bisiesto).
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]  # obtener la cantidad de días para el mes dado.
    # si el mes es febrero y el año bisiesto (feb tiene 29 días).
    if month == 2 and is_year_leap(year):
        res = 29
    return res


# listas con datos de prueba.
test_years = [1900, 2000, 2016, 1987, 2010, 1993]
test_months = [2, 2, 1, 11, 12, 7]
# resultados para cada caso.
test_results = [28, 29, 31, 30, 31, 31]
# bucle para porbar la funcion "days_in_month", con los datos de prueba.
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    # comparacion de los resultados de la funcíon con los resultados esperados.
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
