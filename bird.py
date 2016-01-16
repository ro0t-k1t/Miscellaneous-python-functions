__author__ = 'ronanpiercehiggins'
class Bird:
    def __init__(self, kind, call):

        self._kind = kind
        self._call = call

    def do_call(self, count):
        for i in range(count):
            print 'a %s goes %s' % (self._kind, self._call)



#each time we create an instance of a class, a memroy box is allocated to
#that instance. So the computer knows which box we want to go to, we use
#this. It then directs it towards whichever instance, i.e owl, robbin

owl = Bird('Owl', 'Twit Twoo')

print owl._kind

