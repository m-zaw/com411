import time
import progressbar # please install progressbar2 package "python -m pip install progressbar2"
import cowsay # please install cowsay package "python -m pip install cowsay"

for i in progressbar.progressbar(range(5), redirect_stdout=True):
    print("Loading awesomeness...")
    time.sleep(0.5)

print("What is your name friend?")
name = str(input())
print("That's a wonderful name!")
time.sleep(1.5)
print("Your name have", len(name), "characters.\n")
time.sleep(1.5)

print("How old are you?")
age = (input())
print("That old huh?")
time.sleep(1.5)
age_100 = 100 - int(age)
print("You'll be 100 in", age_100, "years.\n")
time.sleep(1.5)

print("What would you like the turtle to tell you?")
turtle_say = input()

cowsay.turtle("I am independent!\nNo one is going to tell me what to say!")