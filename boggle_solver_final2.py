__author__ = 'ronanpiercehiggins'


from random import choice
from string import ascii_uppercase
import logging
import time
import random
logging.basicConfig(level=logging.INFO)

def timeit(method):
    def timed(*args, **kw):
        t1 = time.time()
        result = method(*args, **kw)
        print '%r %2.7f sec' % (method.__name__, time.time() - t1)
        return result

    return timed



'''letters = ascii_uppercase


newLetters = letters.replace('Q', 'QU')


def get_grid():
    return {(x, y): choice(newLetters) for x in range(X) for y in
                range(Y)}'''


cubes = ['CSOAHP', 'ABBOJO', 'ENSIUE', 'FSKFAP', 'EGAENE', 'YIDSTT', 'ATTOWO', 'TOESIS', 'RHTVWE', 'HLNNRZ', 'MTIOUC', 'NEEHGW', 'DIXRLE', 'YLDERV', 'QHMUNI', 'RETTYL']

def get_grid():
    grid = {}
    for x in range(X):
        for y in range(Y):
            cube = random.choice(cubes)
            chosen_letter = choice(cube)

            if chosen_letter == "Q":
                chosen_letter = "Qu"

            grid[(x,y)] = chosen_letter
    return grid








def get_neighbours():
    neighbours = {}

    for position in grid:
        x, y = position

        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
        (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]

        neighbours[position] = [p for p in positions if
                                0 <= p[0] < X and 0 <= p[1] < Y]

    return neighbours




def path_to_word(path):
    return ''.join([grid[p] for p in path])


def search(path):
    word = path_to_word(path)
    logging.debug('%s: %s' % (path, word))
    if word not in stems:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('%s: skipping %s because in path' % (path, grid[next_pos]))




def get_dictionary():
    stems, dictionary = set(), set()
    with open('bogwords.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)

            for i in range(len(word)):
                stems.add(word[:i + 1])
    return dictionary, stems


@timeit
def get_words():
    for position in grid:
        logging.info('searching %s' % str(position))
        search([position])

    return [path_to_word(p) for p in paths]


def print_grid(grid):
    s = ''
    for y in range(Y):
        for x in range(Y):
            s += grid[x, y] + ' '
        s += '\n'
    print s


size = X, Y = 4, 4
grid = get_grid()
neighbours = get_neighbours()
dictionary, stems = get_dictionary()
paths = []

print_grid(grid)

words = get_words()
print words


@timeit
def find_anagram(word):

    words = []
    with open('bogwords.txt') as f:
        myCounter = 0
        for i in f:
            words.append(i.strip())

    random.shuffle(words)

    for dictionary_word in words:
        if len(dictionary_word) == len(word) and myCounter < 3:
            if (myCounter+1) == 1:
                print "The %sst word of same length is: %s" % (myCounter + 1, dictionary_word)
            elif (myCounter+1) == 2:
                print "The %snd word of same length is: %s" % (myCounter + 1, dictionary_word)

            elif (myCounter+1) == 3:
                print "The %srd word of same length is: %s" % (myCounter + 1, dictionary_word)

            myCounter += 1






def longest_word(arr):
    return max(arr, key=len)


long = longest_word(words)
print "The longest word is '%s'" % long
length_of_word = len(long)
print "This word is %s characters long!" % length_of_word
backwards = long[::-1]
print "This word backwards is %s" % backwards


find_anagram(long)























'''def time_function(method):
    t1 = time.time()
    result = method()
    print '%2.2f sec' % (time.time() - t1)
    return result

words = time_function(get_words)
print words'''





'''def get_grid():
    grid = {}
    for x in range(X):
        for y in range(Y):
            chosen_letter = choice(letters)

            if chosen_letter == "Q":
                chosen_letter == "Qu"

            grid[(x,y)] = chosen_letter


    return {(x, y): choice(newLetters) for x in range(X) for y in
                range(Y)}'''










'''def time_get_words():
    t1 = time.time()
    get_words()
    t2 = time.time()

    total = t2 - t1
    print '%.2f sec' % total


time_get_words()'''