N = int(input("Nechta haqiqiy sonlar kiritmoqchisiz: "))
sonlar = []
for i in range(N):
    son = float(input(f"{i + 1}-sonni kiriting: "))
    sonlar.append(son)
eng_kichik_musbat = None
eng_katta_manfiy = None
for son in sonlar:
    if son > 0:
        if eng_kichik_musbat is None or son < eng_kichik_musbat:
            eng_kichik_musbat = son
    elif son < 0:
        if eng_katta_manfiy is None or son > eng_katta_manfiy:
            eng_katta_manfiy = son
if eng_kichik_musbat is None or eng_katta_manfiy is None:
    print("Manfiy yoq-ku.")
else:
    farq = eng_kichik_musbat - eng_katta_manfiy
    print(f"Eng kichik musbat va eng katta manfiy elementlar orasidagi farq: {farq}")