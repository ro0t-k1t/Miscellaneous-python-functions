__author__ = 'ronanpiercehiggins'


from random import choice
from string import ascii_uppercase

def get_grid():

    return {(x, y): choice(ascii_uppercase) for x in range(size[0]) for y in
                range(size[1])}

def get_dictionary():
    with open('bogwords.txt') as f:
        return  [word.strip().upper() for word in f]

def get_neighbours():
    neighbours = {}

    for position in grid:
        x, y = position

        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
        (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]

        neighbours[position] = [p for p in positions if
                                0 <= p[0] < size[0] and 0 <= p[1] <size[1]]

        #we are creating a loop which makes all the coordinates in the grid, then we filter these coordinates placing the x and y values into p.
    return neighbours


size = X, Y = 2, 2
grid = {(0, 1): 'M', (1, 0): 'E', (0, 0): 'K', (1, 1): 'H'} #get_grid()
neighbours = get_neighbours()


paths = []

path = []

for letter1 in grid:
    path.append(letter1)
    paths.append(path[:])

    for letter2 in neighbours[letter1]:
        path.append(letter2)
        paths.append(path[:])

        for letter3 in neighbours[letter2]:
            path.append(letter3)
            paths.append(path[:])

            for letter4 in neighbours[letter3]:
                path.append(letter4)
                paths.append(path[:])
                path.pop()

            path.pop()
        path.pop()
    path.pop()

for path in paths:
    print ''.join([grid[p] for p in path])



