sonlar = list(map(int, input("Sonlarni probel bilan ajratib kiriting: ").split()))
toq_kopaytma = 1
max_manfiy = None
manfiy = 0
for son in sonlar:
    if son % 2 != 0:
        toq_kopaytma *= son
    if son < 0:
        if max_manfiy is None or son > max_manfiy:
            max_manfiy = son
        manfiy = 1
if manfiy == 0:
    print("Manfiy sonlar mavjud emas")
else:
    farq = toq_kopaytma - max_manfiy
    print(f"Toq sonlar ko'paytmasi va eng katta manfiy son orasidagi farq: {farq}")
