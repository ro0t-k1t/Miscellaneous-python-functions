__author__ = 'ronanpiercehiggins'


from random import choice
from string import ascii_uppercase



import sys
print sys.getrecursionlimit()

import logging
logging.basicConfig(level=logging.DEBUG)

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
grid = get_grid()
neighbours = get_neighbours()


paths = []

def path_to_word(path):
    return ''.join([grid[p] for p in path])

def search(path):
    word = path_to_word(path)
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])


dictionary = get_dictionary()


for position in grid:
    logging.info('searching %s' % str(position))
    search([position])

print [path_to_word(p) for p in paths]
