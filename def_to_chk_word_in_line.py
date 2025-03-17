def check_word_in_line(word):
    data=True
    line_no = 1
    with open("practise.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print("it is in line no.",line_no)
            line_no += 1




check_word_in_line("Prisha")