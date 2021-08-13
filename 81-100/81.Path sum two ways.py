import math

f = open('p081_matrix.txt')
matrix = [[int(number) for number in line.split(',')] for line in f]
unvisited = dict(((i, j), math.inf) for i in range(len(matrix)) for j in range(len(matrix)))
unvisited[(0, 0)] = matrix[0][0]
visited = {}

print(unvisited)
while True:
    node = min(unvisited, key=(lambda x: x[1]))
    i = node[0]
    j = node[1]
    distance = unvisited[node]
    # Below
    if i+1 < len(matrix):
        below_tentative = distance + matrix[i+1][j]
        if below_tentative < unvisited[(i+1, j)]:
            unvisited[(i + 1, j)] = below_tentative

    # Right
    if j+1 < len(matrix):
        right_tentative = distance + matrix[i][j+1]
        if right_tentative < unvisited[(i, j+1)]:
            unvisited[(i, j+1)] = right_tentative

    visited[node] = unvisited.pop(node)
    if len(unvisited) == 0:
        print(visited[(len(matrix)-1, len(matrix)-1)])
        break
