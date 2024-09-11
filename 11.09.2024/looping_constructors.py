# for loop
list=[1,2,3,4,5]

for num in list:
    print(num)

# for loop using range function 
for i in range(4):
    print(i)

# for loop using range function with start, end
for i in range(1,4):
    print(i)

# printing even numbers from 1 to 5 with if condition
for i in range(1,6):
    if i%2==0:
        print(i)

# printing even numbers from 1 to 5 without if condition
for i in range(2,6,2):
        print(i)

# while loop
i = 1
while i < 6:
  print(i)
  i += 1