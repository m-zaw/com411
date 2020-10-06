print("What type of cover does this book have?")
cover_type = input()

if (cover_type == "soft"):
    print("Is the book perfect-bound?")
    perfect_bound = input()

    if (perfect_bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books") 
else:
    print("Books with hard covers can be more expensive!")