def eliminar(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_ar = ""
    for char in texto:
        texto_ar = char + texto_ar
    return texto_ar


def palindromo(texto):
    texto = eliminar(texto)
    texto_ar = reverse(texto)
    return texto == texto_ar


print(palindromo("abba"))
print(palindromo("hola mundo"))
print(palindromo("amo la paloma"))
