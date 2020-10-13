print("Please enter a number?")
number = int(input())

count = 0
total = 1

while ( count < number ):
    count = count + 1
    total = total * count

print("The factorial is", total)