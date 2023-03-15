def find_duplicate():
    x = input("Enter a word = ")
    for char in set(x):
        counts = x.count(char)
        while counts > 1:
            print(char, ":", counts, end=' ')
            break
find_duplicate()
            