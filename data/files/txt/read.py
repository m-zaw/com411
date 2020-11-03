filepath = "C:/Users/Milan/OneDrive - Solent University/SOLENT_L6/Y1/com411/data/files/txt/locations.txt"
def search(filename):
    print("Searching...")
    with open(filename) as file:
        for line in file:
            print(f"Looked in {line}.", end="")
    print('\n'"...Done!")

def run():
    search(filepath)

run()