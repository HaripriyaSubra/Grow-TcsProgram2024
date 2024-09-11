class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
	
emp1 = Employee("John Doe", 30)
emp1.display_info()
