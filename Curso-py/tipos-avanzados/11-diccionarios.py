punto = {"x": 25, "y": 50}  # Diccionario.
print(punto)
print(punto["x"])
# una de las formas de ver los valores ingresados en el diccionario.
print(punto["y"])

# forma de agregar valores a un diccionario ya existente, bajo demanda.
punto["z"] = 45
print(punto)
# print(punto, punto["a"])

# metodo para acceder a un valor del diccionario. y ver si este se encuentra incluido en el.
if "a" in punto:
    print("encontre A", punto["a"])

# otro metodo para poder acceder a un valor del diccionario.
print(punto.get("x"))
# ejemplo si el valor no existe en el diccionario.
# print(punto.get("a"))
# lo mismo que el anterior comentario, pero dandole un valor.
print(punto.get("a", 97))

# metodo de eliminar un llave del diccionario.
del punto["y"]
del (punto["x"])

print(punto)
punto["x"] = 25

# metodo de acceder a todos lo valores de un diccionario.
# for valor in punto:
#    print(valor, punto[valor])

# otro metodo para acceder a los metodos de un diccionario.
for valor in punto.items():
    print(valor)

# igual que arriba, pero dando por separado las llaves y los valores.
for llave, valor in punto.items():
    print(llave, valor)

# uso "real" de diccionarios.
usuarios = [
    {"id": 1, "nombre": "Pablo"},
    {"id": 2, "nombre": "Martin"},
    {"id": 3, "nombre": "Felipe"},
    {"id": 4, "nombre": "Cecilia"},
]

for usuario in usuarios:
    print(usuario["nombre"])
