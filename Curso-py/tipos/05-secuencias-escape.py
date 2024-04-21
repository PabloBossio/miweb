# Escribir lo que sea sin que sea ejecutado.
# \ "" el backslash le dice al lenguaje que lo que sigue de el sea mostardo en los strings, sin ser tomado por una parte del codigo.
# \\
# \'
# \n va a tomar lo que sigue de este comando y pasarlo una linea por debajo de la que se encuentra.

curso = " Ultimate \n\"Python\""
print(curso.lstrip())
