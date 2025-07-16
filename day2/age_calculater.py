from datetime import date
def age(birth_year):
    current_year = date.today().year
    return current_year - birth_year
birth_year = int(input("Enter your birth year: "))
age=age(birth_year)
print(age)
