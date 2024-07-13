'''Python dasturlash tilida 2 xil turdagi fayllar bilan ishlash mumkin.
1. Matnli(text)
2. Binary file

MAtnli fayllar bilan ishlash uchun dastlab, faylni ochish funlsiyasi
open chaqiriladi.

Ushbu open() funksiyasi ikki xil qiymat qabul qiladi:
1. filename - fayl nomi 
2. rejim_mode - faylni ochushdan maqsad

rejim_mode quyidagilardan biri bo;lishi lozim:
rt - Matnli fayllar ma'lumotini o'qish uchun
Ushbu rejim faqat fayldan ma'lumot  o'qishga ruxsat beradi.

ruxsatni tekshirish uchun fwritable() yoki freadable() funksiyalardan birini ishlatish lozim!

faylni ochish rejimi "r" rejimi bo'lishi mumkin:
f = open("example.txt", "r")

# Faylni ochilgan uchun matnning kamchiligi olish

text = f.read()
print(text)

'''

'''
Pyton dasturlash tilida matnli fayllarga faqat str tipidagi ma'lumotlarni yozish mumkin.

Fayllarga ma'lumot yozish uchun write() funksiyasidan foydalaniladi.

# '''
# filename = input("Fayl k-ng:>  ")
# f = open(filename,"wt")
# for x in range(10):
#     f.write(str(x) + " ")

'''writelines() - Faylga ma'lumotlarini kiritish uchun ishlatiladi. 
with bilan ochganda faylni yopish zaruratini olmaydi.


seek(size,whence) - Ushbu funksiya fayl ko'rsatikichining faylning holatiga nisbatan surish uchun islatiladi.
size ning o'rnida ixtiyoriy butun son qatnashishi mumkin.

whence rejimini o'z ichiga qo'shish uchun qiymatlari:
0 - faylnin boshiga nisbatan siltishi 
1 - faylning ko'rsatkichning joriy holatiga nisbatan siljitish
2 - faylning oxiriga nisbatan siljitish





'''
