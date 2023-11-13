# List Comprehensions
numbers = [0, 1, 2, 3, 4]

double_numbers = [x * 2 for x in numbers]
print(double_numbers)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
lower = [friends.lower() for name in friends]

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends.")


# with conditional
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = [
    name.title()
    for name in guests
    if name.lower() in [f.lower() for f in friends]
]

print(present_friends)

# set comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

frieds_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)

# dictionary comprehension
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}
print(long_timers)

# zip
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends, time_since_seen))

print(long_timers)

# enumerate
friends = ["Rolf", "John", "Anne"]

for counter, friend in enumerate(friends): # start from 0, you can use enumerate(friends, start=1)
    print(counter)
    print(friend)