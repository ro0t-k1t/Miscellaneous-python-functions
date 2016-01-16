__author__ = 'ronanpiercehiggins'


num = int(input("Enter a number: "))


if num > 1:

   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print("%s is a prime number" % num)


else:
   print(num,"is not a prime number")
