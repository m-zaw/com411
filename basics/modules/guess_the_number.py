import random as rnd

print("Please enter the minimum value:")
min_num = int(input())

print("Please enter the maximum value:")
max_num = int(input())
r_num = rnd.randrange(min_num, max_num, 1)

print("I am thinking of a number between {} and {}. Can you guess what it is?".format(min_num, max_num))


def play_guess_the_number():
    guess_num = int(input())

    if guess_num == r_num:
        print("Congratulations! You guessed my number!")
    elif guess_num > r_num:
        print("Your guess is too high.")
        print("Try again:")
        play_guess_the_number()
    elif guess_num < r_num:
        print("Your guess is too low.")
        print("Try again:")
        play_guess_the_number()


play_guess_the_number()
