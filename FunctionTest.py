def my_function(fname,lname):
    print('Your first name is:',fname)
first_name = input('Enter your first name : - ')
last_name = input('Enter your last name : - ')
my_function(first_name,last_name)
def my_function1(x):
    x=x+10
    return x
a = int(input('Enter value of x :- '))
print('After adding 10 value of x is :- ',my_function1(a))
add = lambda a,b,c: a+b+c
print(add(10,20,30))
