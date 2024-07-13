def manfiy_sonlar(s):
    return True if s < 0 else False
ls = []
ls = list(map(int,input("List elementlarini kiriting: ").split()))
musbat = list(filter(lambda x: x > 0, ls))
manfiy = tuple(filter(manfiy_sonlar,ls))

print(musbat)

print(manfiy)