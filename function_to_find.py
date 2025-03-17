def check_word(word):
    with open("practise.txt", "r") as f:
        data = f.read()
        if data.find(word) != -1:
            print("Found")
        else:
            print("Not found")

check_word("Prisha")