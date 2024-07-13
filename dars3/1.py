import os
#copy C>: ls = [1,2,3] cp = ls.copy
'''list C> a) ls = []
        b) rht = list()'''
# ls = []
# print(type(ls))
# ls1 = list()
# print(type(ls1))
# af = (1,2,3,4,5,6,7)
# for x in af:
#     ls.append(x)
#     print(ls)
# ls1 = list(af)
# print(ls1)

'''appen(x) - ohiriga qo'shish'''
# cars = ["BMW", "Tico", "Zaporoj", "Rols Roys"]
# cars.append(15)
# cars.append(True)
# cars.append("Akmal tushunmadi")
# cars.append([1,2,3])
# print(cars)
# rs = cars
# print(cars)
# cp = cars.copy()
# print(rs)
# cars.clear()
# print(rs)

#4. count(n) C>: List elementlari orasida n necha marta qatnashganini qaytaradi
#M: ls = [1,2,1,2,3,2]    ls.count(2) = natija>: = 3

#5. remove(x) - Listda qatnashgan x elementini burunchi uchraganini o'chirib beradi.
# ls = [x % 2 for x in range(15)]
# print(ls)
# ls = [x % 4 for x in range(15)]
# print(ls)
# print(ls.count(3))

#kiritilgan sonni o'chirish
# Foydalanuvchidan sonlar ro'yxatini kiritish
ls = list(map(int, input("List elementlarini kiriting>>>: ").split()))
# O'chirilishi kerak bo'lgan sonni kiritish
x = int(input("x = >> "))
# x sonini ro'yxatdan o'chirib tashlash
while x in ls:
    ls.remove(x)
# Natijaviy ro'yxatni chop etish
print(ls)



