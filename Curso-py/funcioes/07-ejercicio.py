# pedirle al programa si una palabra es un palindormo.

def eliminar(texto):  # funcion para eliminar espacios en blanco.
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


# funcion para que el programa lea e itere al reves el string, guardando cada caracter.
def reverse(texto):
    texto_ar = ""
    for char in texto:
        texto_ar = char + texto_ar
    return texto_ar


# funcion para comparar los strings tanto derecho como al revez, y determinar si es o no, un palindromo.
def palindromo(texto):
    texto = eliminar(texto)
    texto_ar = reverse(texto)
    return texto.lower() == texto_ar.lower()


print(palindromo("amo la paloma"))
print(palindromo("abba"))
print(palindromo("Hola mundo"))
print(palindromo("Reconocer"))
