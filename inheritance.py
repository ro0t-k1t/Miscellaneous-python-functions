__author__ = 'ronanpiercehiggins'


class Animal(object):

    def __init__(self):

        print "Animal created"





class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

d = Dog()