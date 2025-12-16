with open("allbooks.txt") as mybooks:
    for line in mybooks:
        print(line.strip().upper())
