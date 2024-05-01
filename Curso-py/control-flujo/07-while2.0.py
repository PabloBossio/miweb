contrag = input("Ingrese la contraseña de su nueva cuenta:")

contrag = int(contrag)

contrai = input("Ingrese la contraseña de su cuenta:")

contrai = int(contrai)

while contrag != contrai:
    print("La contraseña es incorrecta, vuelva a intentar: ")
    contrai = input("* ")
    contrai = int(contrai)

print("Usted a ingresado a su cuenta.")
