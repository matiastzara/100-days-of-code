#list, tuples and sets
list_grades = [80, 75, 90, 100] #mutable
tuple_grades = (80, 75, 90, 100) #immutable
set_grades = {80, 75, 90, 100} #unique and unordered

#dictionary
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

# comma separated values using join
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")