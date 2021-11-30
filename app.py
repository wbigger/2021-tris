#!/usr/bin/env python3

print("Gioco del tic tac toe")

board = [
          ['-','-','-'],
          ['-','-','-'],
          ['-','-','-']
        ]

symList = ['X','O']

def mostra_tabellone():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def win(board):
    for sym in symList:

        #check rows
        for i in range(3):
            if board[i].count(sym)==3:
                return sym

        #check columns
        for i in range(3):
            if (board[0][i]==sym and 
               board[1][i]==sym and
               board[2][i]==sym):
                return sym
        # check diagonals
        if (board[0][0]==sym and
           board[1][1]==sym and
           board[2][2]==sym):
            return sym
        if (board[0][2]==sym and
           board[1][1]==sym and
           board[2][0]==sym):
            return sym
    
    return False


winner=False

for idx in range(9):
    
    symbol = symList[idx%2]

    mostra_tabellone()

    print("Il tuo simbolo è: "+symbol)

    while True:
        r = int(input("Inserisci la riga (valori da 0 a 2): "))
        c = int(input("Inserisici la colonna (valori da 0 a 2): "))
        #  aggiungere anche condizione che r,c devono essere compresi tra 0 e 2
        if board[r][c]=='-':
            board[r][c] = symbol
            break
    winner=win()
    if winner:
        break
        

mostra_tabellone()
print("The winner is... "+winner+"!")
