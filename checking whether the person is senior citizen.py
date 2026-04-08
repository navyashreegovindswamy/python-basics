name= input("enter name of the person: ")
year_of_birth=int(input("enter year of birth: "))
current_year=int(input("enter current year: "))
age=current_year-year_of_birth
print("age of the person is: ", age)
if age >= 60:
    print(name, "is a senior citizen.")
else:
    print(name, "is not a senior citizen.")