sonlar = input("Sonlarni kiriting c>: ").split()
sonlar = [int(x) for x in sonlar]
sonlar.sort()
sonlar.reverse()
juft = [x for x in sonlar if int(str(x)[0]) % 2 == 0]
print("Saralangan sonlar (kamayish tartibida):", sonlar)
print("Birinchi raqami juft bo'lgan sonlar:", juft)

