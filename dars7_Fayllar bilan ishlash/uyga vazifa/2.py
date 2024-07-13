def sezar_shifr(son):
    oddiy = "0123456789"
    shifr = "7890123456"
    jadval = str.maketrans(oddiy, shifr)
    return son.translate(jadval)
foydalanuvchi_son = input("Iltimos, son kiriting: ")
print("Shifrlangan son:", sezar_shifr(foydalanuvchi_son))
