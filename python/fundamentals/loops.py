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


#iterationg over dictionaries
friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")


#break and continue
#break

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print("Shipping new car to customer!")

#continue
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
'''

# Else in loops
cars = ["ok", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")