def birinchi_sozni_ikkita(fayl_nomi):
    with open(fayl_nomi, 'r') as fayl:
        matn = fayl.read().strip()
        birinchi_soz = matn.split()[0]
        return f"{birinchi_soz} {birinchi_soz}"
matn = "Hammaga salom. Bugun dars yaxshi o'tdi. Bugun hamma vazifani bajardi."
with open("matn.txt", 'w') as fayl:
    fayl.write(matn)
print(birinchi_sozni_ikkita("matn.txt"))