'''
numbers = [0, 1, 2, 3, 4]

double_numbers = [x * 2 for x in numbers]
print(double_numbers)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
lower = [friends.lower() for name in friends]
'''
friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends.")