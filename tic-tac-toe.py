
#sin terminar
from random import randrange

board = [[1, 2, 3], [4, "x", 6], [7, 8, 9]]

def display_board(board):
  # La función acepta un parámetro el cual contiene el estado actual del tablero
  # y lo muestra en la consola.
  print("+-------+-------+-------+")
  for row in range(3):
    print("|", end=" ")
    for column in range(3):
      print("",board[row][column],"  |",end="  ")
    print("")
  print("+-------+-------+-------+ ")


display_board(board)
  # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
  # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

def make_list_of_free_fields(board):
  cuadrosVacios = []
  for i in (len(board)):
    for v in range(len(board)):
      if type(board[i][v]) == int:
        cuadrosVacios.append((i,v))

 
def enter_move(board):
    # Pedir la posición al jugador
    while True:
        position = input("Introduce tu posición (1-9): ")
        try:
            position = int(position)
            if 1 <= position <= 9:
                break
            else:
                print("Posición inválida. Debe ser un número entre 1 y 9.")
        except ValueError:
            print("Posición inválida. Debe ser un número.")

    # Convertir la posición a coordenadas de la matriz
    row = (position - 1) // 3
    column = (position - 1) % 3

    # Validar que la casilla esté vacía
    if board[row][column] != "x" and board[row][column] != "o":
      board[row][column] = "o"
    else:
        print("Casilla ocupada. Intenta de nuevo.")

    

    # Mostrar el tablero actualizado
    display_board(board)

# Ejemplo de uso
enter_move(board)

def maquina():
  for i in range(10):
      print(randrange(8))

# def draw_move(board):
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.
   

