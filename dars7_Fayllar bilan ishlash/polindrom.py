def isPolindrom():
    with open("Bitiklar.txt") as g:
        words = g.read().split()
        for word in words:
            if word == word[::-1]:
                print(f"'{word}' is a palindrome")
            else:
                print(f"'{word}' is not a palindrome")
isPolindrom()
