def eng_katta_son(fayl_nomi):
    with open(fayl_nomi, 'r') as fayl:
        sonlar = list(map(int, fayl.readline().strip().split()))
    return max(sonlar)
sonlar = list(range(1, 21))
with open("sonlar.txt", 'w') as fayl:
    fayl.write(" ".join(map(str, sonlar)))
print("Eng katta son:", eng_katta_son("sonlar.txt"))
