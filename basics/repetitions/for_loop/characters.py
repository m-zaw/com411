print("What strange markings do you see?")
markings = input()

print("\nIdentifying...\n")

for count in range(0, len(markings), 1):
    print("index", count, ":", markings[count])