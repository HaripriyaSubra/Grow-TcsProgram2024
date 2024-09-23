import csv 

# write operation to a file
with open("sample.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

# Reading from the file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to the file
with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")

# Reading the updated file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


try:
    with open("example1.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An I/O error occurred.")


persons_data=[
    {'name':'Alice','age':34},
    {'name':'Bobby','age':47}
]

with open('persons.csv','w',newline='') as csvfile:
    header=['name','age']
    writer = csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    writer.writerows(persons_data)