# def mukammal_son(n):
#     if n < 2:
#         return False
#     divisors = [1]  # Mukammal sonning bo'luvchilarini saqlash uchun ro'yxat
#     for i in range(2, int(n**0.5) + 1):  # 2 dan boshlab n ning kvadrat ildizigacha bo'lgan raqamlar
#         if n % i == 0:
#             divisors.append(i)  # i ni bo'luvchilar ro'yxatiga qo'shish
#             if i != n // i:
#                 divisors.append(n // i)  # i ning juft bo'luvchisini ham qo'shish
#     return sum(divisors) == n  # Bo'luvchilarning yig'indisini n ga tengligini tekshirish
# # Misollar
# print(mukammal_son(28))  # True
# print(mukammal_son(27))  # False

def mson(n):
    if n < 2:
        return False
    sonlar = [1] 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sonlar.append(i)
            if i != n // i:
                sonlar.append(n // i)
    return sum(sonlar) == n  
p = int(input("Son>>: "))
if mson(p):
    print(f"{p} Mukammal son")
else:
    print("{p} Mukammal son emas, mana mukammmal sonlar:\n 6,28,496,8128...")