def box(word):
    num_dashes = 6 + len(word)
    print("-" * num_dashes)
    print("|  {}  |".format(word))
    print("-" * num_dashes)


def uppercase(word):
    print(word.upper())


def lowercase(word):
    print(word.lower())


def mirror(word):
    reverse_word = ""
    for letter in reversed(word):
        reverse_word += letter
    print("{} | {}".format(word, reverse_word))


box("hello world")
uppercase("hello world")
lowercase("hello world")
mirror("hello world")
