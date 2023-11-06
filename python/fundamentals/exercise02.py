# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for i in range (1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
        continue
    if i % 5 ==0:
        print("Buzz")
        continue
    print(i)