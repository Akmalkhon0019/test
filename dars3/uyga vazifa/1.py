a = int(input("a => "))
b = int(input("b => "))
sonlar = [x for x in range(a, b+1) if x % 2 == 0]
print(sonlar)
