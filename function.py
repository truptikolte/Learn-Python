# define a function
def add(num1,num2):
    sum = num1 + num2
    print('Addition: ',sum)
    return
def subtract(num1,num2) :
    sub = num1-num2
    print('Subtraction: ',sub)
def multiply(num1,num2) :
    mult = num1*num2
    print ('multiplication :',mult)
def division(num1,num2):
    div = num1/num2
    return div
#print('enter first number :')
a = int(input('Enter first number :'))
#print('enter second number')
b = int(input('Enter second number :'))
add(a,b)
subtract(a,b)
multiply(a,b)
print('Division : ',division(a,b))