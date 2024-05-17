# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

# toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# si es par, evalúa un nuevo c0 como c0 ÷ 2;
# de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

# Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.

# Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.

# Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito.

n1 = int(input("Ingrese el número a tratar : "))
# creamos una varible en 0 para poder utilizar en while y asignarle los valores correspondientes.
c0 = 0

if n1 > 0:  # hacemos que n1 sea c0 para simplicar el programa
    c0 = n1

counter = 0  # creamos una variable en cero que actuara como contador.
while c0 != 1:
    if c0 % 2 == 0:        # implementamos el metodo de Collatz
        c0 = c0 // 2
        print(c0)
    else:
        c0 = c0 * 3 + 1
        print(c0)
    counter += 1

print(f"{c0} \nPasos: {counter}")
