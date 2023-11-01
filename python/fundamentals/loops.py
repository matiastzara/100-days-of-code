#while loop
'''
user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")
'''
#for loop
'''
students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80}
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")
'''

#destructuring
'''
friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for name, age in friends:
    print(f"{name} is {age} years old.")
'''

#iterationg over dictionaries
friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")