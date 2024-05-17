# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

# Se puede usar tanto con bucles while y for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

# un bucle for;
# el concepto de ejecución condicional (if-elif-else).
# la sentencia continue.
# Tu programa debe:

# pedir al usuario que ingrese una palabra.
# utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
# utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
# Prueba tu programa con los datos que le proporcionamos.
# Pedimos al usuario que ingrese un string de una palabra para sacarle las vocales.
word_whitout_vowels = input(
    """Ingrese la palabra a la cual desee quitar las vocales:
 """)
word_whitout_VO = ""  # Variable vacía para poder guardar las letras consonantes de la palabra.
# creamos un for que itere los valores de cada letra del string.
for letter in word_whitout_vowels.lower():
    if letter.lower() == "a":  # le indicamos que letras pueden deben ser omitidas
        continue
    elif letter.lower() == "e":
        continue
    elif letter.lower() == "i":
        continue
    elif letter.lower() == "o":
        continue
    elif letter.lower() == "u":
        continue
    else:
        word_whitout_VO += str(letter)

print(word_whitout_VO)
