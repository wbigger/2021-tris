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

mostra_tabellone()

print("Il tuo simbolo è: X")
r = int(input("Inserisci la riga (valori da 0 a 2): "))
c = int(input("Inserisici la colonna (valori da 0 a 2): "))

board[r][c] = 'X'

mostra_tabellone()
