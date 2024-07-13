# brends = ["Jeep", "BMW", "Audi", "Mersede-Benz", "Chevrolet", "Tayota", "Kia"]
# # print(sorted(brends))
# print(brends)
# # print(sorted(brends, reverse=(True)))

# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
# print("Mashina brendlari soni: ",len(brends))

# sonlar = list(range(0,10)) # 
# print(sonlar)

# toq_sonlar = list(range(1,11,2))

# print(toq_sonlar)

# ochiqaruvchi_sonlar = list(range(10,0,-1))
# print(ochiqaruvchi_sonlar)

# juft_sonlar = list(range(0,10,2))
# print(juft_sonlar)

# narhlar = list(range(5600,1000000,99990))
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# print(brends[0:3]) #boshidan to 3 gacha korsatadi, 3chini o'zi chiqmaydi
# print(brends[3:])#3 boshlab ohirigacha
# print(brends[2:5])

# print(brends)
# cars = brends
# print(cars)
# cars.remove("Chevrolet")
# cars.append("Volvo")
# print(cars)
# print(brends) # cars va brend xotiradan bitta joy egalladi - bir xil ma'lumot chiqaradi

# cars = ['lacetti', 'jentra', 'cobalt', 'captiva', 'malibu']
# print(cars)
# my_cars = cars[:]#copy
# print(my_cars)
# my_cars.remove('lacetti')
# print(my_cars)
# print(cars) #copy olinadi /alohida joy oladi

#TUPLE - o'zgarmas ro'yhat

toys = ('car', 'pistolet', 'teddy','icecream')
# print(toys) 
#tuple ga yangi quymat qo'shib yoki o'chirib bo'lmaydi bo'lmaydi
#o'zgartirish uchun tuple ni listga o'zgartiramiz
toys = list(toys)
toys.append('lion')

print(type(toys))
print(toys)
toys = tuple(toys)
print(type(toys))

