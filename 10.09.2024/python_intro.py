print('Welcome to introduction to python session')

a=5
b=10

# check the type of a variable
print(type(a))
print(type(b))

c=10.5
print(type(c))

# type conversion  
int_var = int(c)
print(int_var)
print(type(int_var))

d=True
print(type(d))

e ='welcome to python'

print(type(e))

def find_sum(num1,num2):
    print(num1 + num2)
    #print(f'sum of 2 numbers {num1} and {num2} is {num1+num2}')
    #print('sum of 2 numbers %d and %d is %d' % (num1, num2,num1+num2))

find_sum(a,b)

def greeting():
    name = input('Enter your name: ')
    print(f'Hello {name}. Welcome to the intdodution to python section')

greeting()







