#  Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

# # La semilla de la función ya se muestra en el código esqueleto del editor.

# # Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

# # El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.

def year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2010, 1976, 2004, 2013]
test_result = [False, False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, '->', end="")
    result = year_leap(yr)
    if result == test_result[i]:
        print("OK")
    else:
        print("Fallido")
