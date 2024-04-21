pesos = input("¿Cuanto dinero tienes?")

pesos = int(pesos)

if pesos >= 500:
    print("Puedes comprar una coca")
elif pesos >= 350:
    print("No te alcanza para una coca, pero puede comprar una pepsi por 350, o una manaos por 200")
elif pesos >= 200:
    print("No te alcanza para una coca, pero puedes comprar una manaos por 200")
else:
    print("No te alcanza para ninguna gaseosa")
