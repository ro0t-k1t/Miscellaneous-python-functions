__author__ = 'ronanpiercehiggins'

arr = []
arr2 = []
for i in range(100, 401):

    arr.append(str(i))


for i in arr:

    if int(i[0]) % 2 == 0 and int(i[1]) % 2 == 0 and int(i[2]) % 2 == 0:

        arr2.append(i)

print "The numbers with all even digits are: %s" % arr2






