print("Program Started!")
print("Please enter an ASCII code:")

ascii_code = abs(int(input()))
character = chr(ascii_code)

if ascii_code in range(32,126,1):
    print("The character represented by the ASCII code {} is {}.".format(ascii_code, character))
else:
    print("You have enetered an ASCII code number that is out of range!")