def sozlar_va_gaplar_soni(matn):
    sozlar_soni = len(matn.split())
    gaplar_soni = matn.count('.') + matn.count('!') + matn.count('?')
    return sozlar_soni, gaplar_soni
foydalanuvchi_matn = input("Matn kiriting: ")
with open("matn.txt", 'w') as fayl:
    fayl.write(foydalanuvchi_matn)
sozlar_soni, gaplar_soni = sozlar_va_gaplar_soni(foydalanuvchi_matn)
print(f"So'zlar soni: {sozlar_soni}, Gaplar soni: {gaplar_soni}")
