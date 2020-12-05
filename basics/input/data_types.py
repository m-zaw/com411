print(("What is your name human?"))
name = str(input())

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = int(input())

bmi = weight / (height ** 2)
print(name, "you are", age, "years old and your bmi is", bmi)
