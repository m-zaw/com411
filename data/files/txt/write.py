def search(filename):
    print("Searching... ", end="")

    sections = []
    books = []

    with open(filename) as file:
        for line in file:
            if line.startswith("Section"):
                parts = line.split(":")
                sections.append(parts[1].replace("\n", ""))
            else:
                books.append(line.replace("\n", ""))

    print("Done!")
    return (sections, books)


def save(filename, data):
    print("Saving... ", end="")

    with open(filename, "w") as file:
        file.write("Sections: ")
        for section in data[0]:
            file.write(f"{section},")

        file.write("\nBooks: ")
        for books in data[1]:
            file.write(f"{books},")
    print("Done!")


def run():
    data = search("data/files/txt/books.txt")
    save("data/files/txt/section-books.txt", data)


run()
