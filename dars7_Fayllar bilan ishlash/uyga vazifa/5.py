import random
def musbat_manfiy_fayl():
    ls = [random.randint(-50, 50) for _ in range(10)]
    musbat = [son for son in ls if son > 0]
    manfiy = [son for son in ls if son < 0]
    with open("Musbat.txt", 'w') as musbat_fayl:
        musbat_fayl.write(" ".join(map(str, musbat)))
    with open("Manfiy.txt", 'w') as manfiy_fayl:
        manfiy_fayl.write(" ".join(map(str, manfiy)))
    return musbat, manfiy
musbat, manfiy = musbat_manfiy_fayl()
print("Musbat faylda:", musbat)
print("Manfiy faylda:", manfiy)
