from datetime import date

def check_validity_to_vote(birth_year, voting_age=18):
    try:
        today = date.today()
        age = today.year - int(birth_year)

        if age >= voting_age:
            return "Congrats. You are allowed to vote"
        else:
            return "Sorry. You are too young to vote"
    except ValueError:
        return "Invalid input. Please enter a valid birth year as a number."

# Example usage
birth_year_input = input("Enter your birth year: ")
result = check_validity_to_vote(birth_year_input)
print(result)


def triangle_type(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        if side1 == side2 == side3:
            return "Equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a triangle"

print(triangle_type(5, 5, 8))

print(triangle_type(5, 5, 5))

print(triangle_type(3, 4, 5))

print(triangle_type(1, 1, 3))



