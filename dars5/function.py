'''
Python dasturlash tilida funksiya 2xil:
1. Qiymat qaytaradigan
2. Qiymat qaytarmaydigan
Funksiyani hosil qilish uchun def 
kalit so'zidan foydalaniladi.

Funksiya uchun qo'yilgan talabga mos 
algorutm yoziladi
'''
#Funksiya yaratish quyidagicha:
#def function_name(formal parametrs):
# def daraja(a,b):
#     res = 1
#     for x in range(b):
#         res = res * a
#     return res
# if __name__ == "__main__":
#     x,y = map(int,input("c>>: ").split())
#     print(f"{x}^{y} = {daraja(x,y)}")

# def local_maximum(ls):
#     if type(ls) != list:
#         return
#     for x in range(1,len(ls) - 1):
#         if ls[x] > ls[x-1] and ls[x] > ls[x+1]:
#             print(ls[x], end = " ")

# if __name__ == '__main__':
#     ls = [12,90,45,58,42,65,30,17]
#     print(ls)
#     local_maximum(ls)

def orta_arifmetik(ls:list):
    if type(ls) != list:
        return
    avg = sum(ls)/len(ls)
    print(f"\t\tListning o'rta arifmetik {avg} dan katta qiymatlari")
    for x in ls:
        if x > avg:
            print(f"{x} ", end = " ")
    print(f"\t\tListning o'rta arifmetik {avg} qiymatdan kichik bo'lgan qiymatlari")
    for x in ls:
        if x < avg:
            print(f"{x} ", end = " ")
ls = list(map(int,input("Element C>> : ").split()))
orta_arifmetik(ls)            