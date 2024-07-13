sonlar = list(map(int, input("Sonlarni probel bilan ajratib kiriting: ").split()))
karrali_sonlar_sanog'i = 0
for son in sonlar:
    if son % 3 == 0 or son % 5 == 0 or son % 7 == 0:
        karrali_sonlar_sanog'i += 1
if karrali_sonlar_sanog'i >= 2:
    print("Ketma-ketlikda 3, 5 va 7 ga karrali kamida ikkita son bor.")
else:
    print("Ketma-ketlikda 3, 5 va 7 ga karrali ikkita son yo'q.")
