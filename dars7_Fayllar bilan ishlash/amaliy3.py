#Biror bir tekst faylda yozilgan matnni o’chirmay 
# unga yana matn qo’shuvchi dastur tuzing.

def faylga_qosh(fayl_nomi, yangi_matn):
    with open(fayl_nomi, 'a') as fayl:
        fayl.write(yangi_matn + '\n')
fayl_nomi = "Bitiklar.txt"
yangi_matn = "Yangi qo'shilgan matn"

faylga_qosh(fayl_nomi, yangi_matn)
print(f"Matn '{yangi_matn}' faylga qo'shildi.")
