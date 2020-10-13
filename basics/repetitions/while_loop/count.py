print("How many live cables should I avoid?")
cables_to_avoid = int(input())

cables_avoided = 0

print()

while (cables_avoided < cables_to_avoid):
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print("Done!", cables_avoided, "cables avoided.")