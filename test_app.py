from app import win

def test_win_1():
    board = [
              ['X','X','X'],
              ['-','O','O'],
              ['-','-','-']
            ]
    assert win(board) == 'X'

def test_win_2():
    board = [
              ['X','X','-'],
              ['O','O','O'],
              ['-','-','-']
            ]
    assert win(board) == 'O'

# tanti altri test_win

def test_win_fail_1():
    board = [
              ['X','X','-'],
              ['O','O','-'],
              ['-','-','-']
            ]
    assert win(board) == False


test_win_1()
test_win_2()
# aggiungi altri test... 
test_win_fail_1()
