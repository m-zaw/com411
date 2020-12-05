print("Please enter the first whole number?")
a = int(input())

print("Please enter the second whole number?")
b = int(input())

print("Please enter the third whole number?")
c = int(input())

even_numbers = 0
odd_numbers = 0

if (a % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (b % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (c % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

print("There were {} even and {} odd numbers.".format(even_numbers, odd_numbers))
