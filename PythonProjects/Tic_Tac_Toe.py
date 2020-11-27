#! python 3.7.14
# tic-tac-toe game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

player = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + player + '. Move on which space?')
    move = input()
    theBoard[move] = player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
printBoard(theBoard)