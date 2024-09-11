# handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# handling type error
x = 5
y = "hello"
try:
    z = x/y
except TypeError:
    print("Error: cannot divide an int and a str")

# catching a specific exception
try:
    a = int(input('Enter 1st number:'))
    b = int(input('Enter 2nd number:'))
    division = a/b
except ValueError:
    print("Error: please  provide integer values")
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    k = 5//0 
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')
