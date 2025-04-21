import random

def validating_board(board):
    try:
        for i in range(9):
            sum = 0
            for j in range(9):
                sum += board[i][j]
            if sum != 45:
                return False
        for i in range(9):
            sum = 0
            for j in range(9):
                sum += board[j][i]
            if sum != 45:
                return False
        for a in range(0,9,3):
            for b in range(0,9,3):
                sum = 0
                for i in range(a, a + 3):
                    for j in range(b, b + 3):
                        sum += board[i][j]
                if sum != 45:
                    return False
    except TypeError as e:
        return False
    return True

def create_new_board():
    board = [[None for _ in range(9)] for _ in range(9)]
    n = random.randint(1, 1091)
    with open("src/problems.txt",'r') as file:
        lines = file.readlines()
        line = lines[n]
    g = 0
    for i in range(9):
        for j in range(9):
            if line[g] != '0':
                board[i][j] = int(line[g])
            g += 1
  
    return board


