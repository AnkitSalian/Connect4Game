'''
Project 1
A Simple Game: Connect4
'''
from termcolor import colored

X = colored('X', 'red')
O = colored('O', 'yellow')

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def print_board():
    global board
    for i, row_elems in enumerate(board):
        for j, column_elems in enumerate(row_elems):
            if j == 6:
                print(column_elems)
            else:
                print(column_elems+'|', end="")
        if i != 5:
            print('-'*13)

def check_win(board, coin):
    #Horizontal
    for c in range(len(board[0]) - 3):
        for r in range(len(board)):
            if ((board[r][c] == coin) and (board[r][c+1] == coin) and (board[r][c+2] == coin) and (board[r][c+3] == coin)):
                return True

    #Vertical
    for c in range(len(board[0])):
        for r in range(len(board) - 3):
            if ((board[r][c] == coin) and (board[r+1][c] == coin) and (board[r+2][c] == coin) and (board[r+3][c] == coin)):
                return True

    #Positive Diagonal
    for c in range(len(board[0]) - 3):
        for r in range(len(board) - 3):
            if ((board[r][c] == coin) and (board[r+1][c+1] == coin) and (board[r+2][c+2] == coin) and (board[r+3][c+3] == coin)):
                return True

    # Negative Diagonal
    for c in range(len(board[0]) - 3):
        for r in range(3, len(board)):
            if ((board[r][c] == coin) and (board[r - 1][c + 1] == coin) and (board[r - 2][c + 2] == coin) and (board[r - 3][c + 3] == coin)):
                return True

    return False

def insert_coin(column_index, coin):
    global board
    for i in range(6, 0, -1):
        if board[i-1][column_index-1] == ' ':
            board[i-1][column_index-1] = coin
            print_board()
            return True
    return False

player = 1
print_board()
while True:
    print('Enter the column number from 1 to 7')
    move = int(input(f'Player {player} play your move: '))
    if insert_coin(move, X if player == 1 else O):
        pass
        if check_win(board, X if player == 1 else O):
            print(f'Player {player} won the game')
            break
        else:
            if player == 1:
                player = 2
            else:
                player = 1