def oxirgi_sozni_ikkita(fayl_nomi):
    with open(fayl_nomi, 'r') as fayl:
        matn = fayl.read().strip()
        oxirgi_soz = matn.split()[-1]
        return f"{oxirgi_soz} {oxirgi_soz}"
print(oxirgi_sozni_ikkita("matn.txt"))
