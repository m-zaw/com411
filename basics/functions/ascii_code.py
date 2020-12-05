print("Program Started!")
print("Please enter a standard character:")

letter = input()
value = ord(letter)

if len(letter) == 1:
    print("The ASCII code for {} is {}.".format(letter, value))

print("Program Ended!")
