__author__ = 'ronanpiercehiggins'

def fact(num):

    factorial = 1

    for i in range(1, num+1):

        factorial=factorial*i

    return factorial


print fact(5)

