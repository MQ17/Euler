import math
import copy

def is_triangle(n):
    p = (math.sqrt(1+8*n)-1)/2
    return p.is_integer()


def is_square(n):
    p = math.sqrt(n)
    return p.is_integer()


def is_pentagon(n):
    p = (math.sqrt(1+24*n)+1)/6
    return p.is_integer()


def combinations(things):
    if len(things) == 1:
        return [things]
    combos = []
    for i in range(len(things)):
        subthings = things.copy()
        thing = subthings.pop(i)
        for subcombo in combinations(subthings):
            combos.append([thing] + subcombo)
    return combos


# Generate Dictionaries that match last two digits of a number to first two of some other figurate
blank_dictionary = dict((str(i), []) for i in range(100))
dictionaries = [copy.deepcopy(blank_dictionary) for i in range(5)]
for n in range(100):
    figurates = [n*n, n*(3*n-1)//2, n*(2*n-1), n*(5*n-3)//2, n*(3*n-2)]
    for i in range(5):
        string = str(figurates[i])
        if len(string) == 4 and figurates[i]%100>9:
            dictionaries[i][string[:2]].append(string)


combos = combinations([0, 1, 2, 3, 4])[:60]


def check_loop(triangle, combo):
    triangle = str(triangle)
    possible_squares = dictionaries[combo[0]][triangle[2:]]
    for square in possible_squares:
        possible_pentagons = dictionaries[combo[1]][square[2:]]
        for pentagon in possible_pentagons:
            possible_hexagons = dictionaries[combo[2]][pentagon[2:]]
            for hexagon in possible_hexagons:
                possible_heptagons = dictionaries[combo[3]][hexagon[2:]]
                for heptagon in possible_heptagons:
                    possible_octagons = dictionaries[combo[4]][heptagon[2:]]
                    for octagon in possible_octagons:
                        # print(triangle, square, pentagon, hexagon, heptagon, octagon, combo)
                        if octagon[2:] == triangle[:2]:
                            print(triangle, square, pentagon, hexagon, heptagon, octagon)
                            return triangle, square, pentagon, hexagon, heptagon, octagon
    return -1


# Loop through all the Triangle Numbers
for n in range(45, 141):
    triangle = n * (n + 1) // 2
    if triangle % 100 < 10:
        continue
    # Loop through all dictionaries
    for combo in combos:
        answer = check_loop(triangle, combo)
        if answer != -1:
            print(sum(int(number) for number in answer))


