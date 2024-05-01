def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


l = largo("Hola mundo")
print(f"El strinig de \"hola mundo\" tiene {l} caracteres.")
