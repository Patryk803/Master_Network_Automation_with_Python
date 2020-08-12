with open('configuration.txt', 'r') as file:
    file.seek(4)
    word = file.read(5)
    print(word)

## With function closes the file automatically
