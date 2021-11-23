#!/usr/bin/env python3

print("Gioco del tic tac toe")

board = [
          ['-','-','-'],
          ['-','-','-'],
          ['-','-','-']
        ]


def mostra_tabellone():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

symList = ['X','O']

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
        