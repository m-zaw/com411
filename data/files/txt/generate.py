def search(filename):
    print("Searching...")
    data = {}
    with open(filename)as file:
        section_name = ""
        split = ""
        for line in file:
            if line.startswith("Section"):
                split = line.split(":")
                section_name = split[1].strip()
            else:
                if (section_name in data):
                    values = data[section_name]
                    values.append(line.strip())
                else:
                    data[section_name] = [line.strip()]
    print("Done!")
    return data


def run():
    data = search("data/files/txt/books.txt")

    with open("data/files/txt/generated.csv", "w")as file:
        for item in data.items():
            section = item[0]
            books = item[1]
            file.write(section)
            for book in books:
                file.write(", {}".format(book))
            file.write("\n")


run()
