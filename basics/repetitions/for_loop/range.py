print("What level of brightness is required?")
brightness_desired = int(input())

print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 2):
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)
    
print("Adjustments complete!")