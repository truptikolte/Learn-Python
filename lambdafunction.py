# lambda function
# single line function
x = lambda a,b: a*b
print(x(4,5))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
print(mytripler(10))