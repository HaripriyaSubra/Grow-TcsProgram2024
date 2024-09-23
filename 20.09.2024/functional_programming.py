import random 
from functools import reduce
# 5 random numbers from 1 to 100
numbers = [random.randint(1,100) for _ in range(5)]

print(numbers)

square_numbers = list(map(lambda x: x**2 ,numbers))

print(square_numbers)

even_numbers = list(filter(lambda x : x%2 ==0,numbers))

print(even_numbers)

sum_all = reduce(lambda x,y : x + y, numbers)

print(sum_all)

