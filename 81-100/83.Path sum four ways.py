import math

f = open('p083_matrix.txt')
matrix = [[int(number) for number in line.split(',')] for line in f]
# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]
unvisited = dict(((i, j), math.inf) for i in range(len(matrix)) for j in range(len(matrix)))
unvisited[(0, 0)] = matrix[0][0]
visited = {}

print(unvisited)
while True:
    node = min(unvisited, key=(lambda key: unvisited[key]))
    print(node)
    i = node[0]
    j = node[1]
    distance = unvisited[node]
    # Below
    if i+1 < len(matrix) and (i+1, j) in unvisited:
        below_tentative = distance + matrix[i+1][j]
        if below_tentative < unvisited[(i+1, j)]:
            unvisited[(i+1, j)] = below_tentative
            print("Below", unvisited[(i+1, j)])

    # Above
    if i-1 >= 0 and (i-1, j) in unvisited:
        above_tentative = distance + matrix[i-1][j]
        if above_tentative < unvisited[(i-1, j)]:
            unvisited[(i-1, j)] = above_tentative
            print("Above", unvisited[(i-1, j)])

    # Right
    if j+1 < len(matrix) and (i, j+1) in unvisited:
        right_tentative = distance + matrix[i][j+1]
        if right_tentative < unvisited[(i, j+1)]:
            unvisited[(i, j+1)] = right_tentative
            print("Right", unvisited[(i, j+1)])

    # Left
    if j-1 >= 0 and (i, j-1) in unvisited:
        left_tentative = distance + matrix[i][j-1]
        if left_tentative < unvisited[(i, j-1)]:
            unvisited[(i, j-1)] = left_tentative
            print("Left", unvisited[(i, j-1)])

    visited[node] = unvisited.pop(node)
    if len(unvisited) == 0:
        print(visited[(len(matrix)-1, len(matrix)-1)])
        break
