# Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

# Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

# pedirá al usuario que ingrese un número entero;
# utilizará un bucle while;
# comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
# ¡El mago está contando contigo! No lo decepciones.

secret_number = 777

number = input(
    """
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
number = int(number)
# iniiciamos el while haciendo que este interprete y compare el valor ingresado por el usuario con el numero secreto.
while number != secret_number:
    # le indicamos el msj en caso de que no el usuario no adivine.
    print("!Ja Ja¡, !Estas atrapado en mi bucle¡")
    number = input("Intentalo hasta que lo logres JAJAJA: ")
    number = int(number)  # hacemos que el usuario vuelva a intentar.

print("!Bien hecho¡, lo has logrado muggle, eres libre ahora.")
