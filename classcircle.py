__author__ = 'ronanpiercehiggins'


class Circle(object):

    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.perimeter = 2 * Circle.pi * self.radius


    def calc(self):

        return Circle.pi * (self.radius ** 2)

    def set_radius(self, new_radius):

        self.radius = new_radius



c = Circle(radius=3)
#b = Circle()

#print c.calc()


#c.set_radius(3)
print c.radius
print c.calc()

print c.perimeter

"""print b.pi
print b.radius
print c.radius"""

