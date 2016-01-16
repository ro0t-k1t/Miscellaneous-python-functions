__author__ = 'ronanpiercehiggins'

class Bird:
    def __init__(self, kind, call):

        self._kind = kind
        self._call = call

    def do_call(self):
        print 'a %s goes %s' % (self._kind, self._call)


class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.learned_phrases = set()

    def learn_phrase(self, phrase):
        self.learned_phrases.add(phrase)

    def do_call(self):
        Bird.do_call(self)
        print '\n'.join(self.learned_phrases)



class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __repr__(self):
        return '%s/%s' % (self.num, self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)





f1 = Fraction(1,2)
f2 = Fraction(1,4)

f3 = f1 + f2

print f3


parrot = Parrot()

parrot.do_call()

parrot.learn_phrase("Squak Squak Squak")

parrot.do_call()

parrot.learn_phrase("Squak Squak Squak")

parrot.do_call()

parrot.learn_phrase("Im a parrot!")

parrot.do_call()





