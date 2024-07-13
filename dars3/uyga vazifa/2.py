a = int(input("a => "))
b = int(input("b => "))
sonlar = [x for x in range(a, b+1) if x % 2 == 1]
sonlar.reverse()
print(sonlar)