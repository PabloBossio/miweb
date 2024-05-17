# Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

# La semilla de la función ya se muestra en el código esqueleto del editor.

# Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

# El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.
# Esta funcion determina si un año es bisiesto o no.
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# lista con los datos de prueba.
test_data = [1900, 2000, 2016, 1987]
# lista con los resultados.
test_results = [False, True, True, False]
# recorro la lista de datos para comprobar la función.
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    # llamado a la función "is_year_leap", para obtener el resultado.
    result = is_year_leap(yr)
    # Comparamos los resultados de la funcion con la lista de resultados.
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
