__author__ = 'ronanpiercehiggins'


class Dog(object):

    species = "mammmal" #class object attributes

    def __init__(self, breed, age):

        self.breed = breed
        self.age = age


    def rand(self):

        Breed2 = self.breed

        return Breed2









Molly = Dog(breed="Cocker Spaniel", age='10')
Toby = Dog(breed="Alsation", age='20') #creates instance of dog


print Dog.rand(Molly)
print Dog.rand(Toby)

print Toby.age #doesnt use parentheses because its an attribute on the object
print Molly.age

print Toby.species
print Molly.species


