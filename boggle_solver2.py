from random import choice
from string import ascii_uppercase


def get_grid():

    return {(x, y): choice(ascii_uppercase) for x in range(size[0]) for y in
                range(size[1])}


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
grid = get_grid()
neighbours = get_neighbours()


paths = []

def path_to_word(path):
    return ''.join([grid[p] for p in path])

def search(path):
    if len(path) > size [0] * size[1]:
        return

    paths.append(path)
    for next_pos in neighbours[path[-1]]: #minus 1 signifies the last element of an array
        search(path + [next_pos])

for position in grid:
    search([position])

for path in paths:
    print ''.join([grid[p] for p in path])
