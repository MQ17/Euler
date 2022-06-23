f = open("81-100\\p096_sudoku.txt", "r")
f.readline()
board = []
for i in range(9):
    board.append(list(map(int, list(f.readline())[:-1])))

empty_squares = []
for i in range(9):
    for j in range(9):
        if board[i][j]:
            empty_squares.append((i,j))

n = 0
while True:
    current = empty_squares[n]
    for i in range(1, 10):
        board[current[0]][current[1]] = i
        if (len(board[0]) == len(set(board[0]))):


