from random import randrange

board = [[1, 2, 3], [4, "x", 6], [7, 8, 9]]

def display_board(board):
    """
    Muestra el tablero en la consola.
    """
    print("+-------+-------+-------+")
    for row in range(3):
        print("|", end=" ")
        for column in range(3):
            print("", board[row][column], "  |", end="  ")
        print("")
    print("+-------+-------+-------+ ")

def make_list_of_free_fields(board):
    """
    Crea una lista de las casillas vacías del tablero.
    """
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board)):
            if type(board[i][j]) == int:
                free_fields.append((i, j))
    return free_fields

def enter_move(board, symbol):
    """
    Solicita al jugador (o a la IA) que ingrese una posición y la marca en el tablero.
    """
    while True:
        if symbol == "o":
            position = input("Introduce tu posición (1-9): ")
        else:
            position = randrange(1, 10)  # IA elige al azar
        try:
            position = int(position)
            if 1 <= position <= 9:
                break
            else:
                print("Posición inválida. Debe ser un número entre 1 y 9.")
        except ValueError:
            print("Posición inválida. Debe ser un número.")

    row = (position - 1) // 3
    column = (position - 1) % 3

    if board[row][column] != "x" and board[row][column] != "o":
        board[row][column] = symbol
    else:
        print("Casilla ocupada. Intenta de nuevo.")

    display_board(board)

def check_win(board, symbol):
    """
    Verifica si el jugador con el símbolo dado ha ganado.
    """
    # Revisar filas
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol:
            return True

    # Revisar columnas
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == symbol:
            return True

    # Revisar diagonales
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

def check_tie(board):
    """
    Verifica si el juego ha terminado en empate.
    """
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                return False
    return True

def play_game():
    """
    Función principal del juego.
    """
    current_symbol = "x"  # La máquina comienza
    while True:
        enter_move(board, current_symbol)

        if check_win(board, current_symbol):
            print(f"¡{current_symbol} gana!")
            break

        if check_tie(board):
            print("Empate!")
            break

        if current_symbol == "x":
            current_symbol = "o"  # Cambio de turno al jugador
        else:
            current_symbol = "x"  # La máquina juega de nuevo

if __name__ == "__main__":
    play_game()
