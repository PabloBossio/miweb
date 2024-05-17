# crea un programa que nos de un tablero de ajedrez y sea jugable.
empty = ''
board = []
# lista creada para columnas.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# lista para encabezado de columnas.
header = [''] + letters
# agrego el encabezado al tablero.
board.append(header)

board += [
    ['8', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['7', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['6', empty, empty, empty, empty, empty, empty, empty, empty],
    ['5', empty, empty, empty, empty, empty, empty, empty, empty],
    ['4', empty, empty, empty, empty, empty, empty, empty, empty],
    ['3', empty, empty, empty, empty, empty, empty, empty, empty],
    ['2', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['1', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

for row in board:
    row_str = ' '
    for item in row:
        row_str += str(item) + ' '
    print(row_str)
