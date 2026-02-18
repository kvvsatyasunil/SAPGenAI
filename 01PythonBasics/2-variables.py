from datetime import datetime


name = "Sunil"
age = 30    
height = 5.9
is_student = False

print("Name: ", name, " is of type ", type(name))
print("Age: ", age, " is of type ", type(age))
print("Height: ", height, " is of type ", type(height))
print("Is Student: ", is_student, " is of type ", type(is_student))

age_str = "56"
print("Age as string: ", age_str, " is of type ", type(age_str))

age_int = int(age_str)  # Convert string to integer
print("Age as string: ", age_int, " is of type ", type(age_int))

newage = input("Enter your age: ")
if int(newage) > 18:
    print(name, "is an adult.")
elif int(newage) == 18:
    print(name, "is just an adult.")
else:   
    print(name, "is not an adult.")

print(f"{name} with height {height} is an adult. {datetime.now()} ") # f-string, when we want to include variables in string