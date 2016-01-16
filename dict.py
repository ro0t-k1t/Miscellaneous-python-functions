__author__ = 'ronanpiercehiggins'


def get_dictionary():
    with open('bogwords.txt') as f:
        return  [word.strip().upper() for word in f]


get_dictionary()