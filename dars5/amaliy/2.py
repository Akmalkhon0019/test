# Quyidagi list elementlarini raqamlari yig’indisi bo’yicha
# tartiblab, natijasini ekranga chiqaruvchi dastur yarating.
ls = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sortlist = sorted(ls,key = lambda x:(x/10)+(x%10))
print(sortlist)
zz = [123,451,22,1,47,6655,145,214,89,14]
sortlist2 = sorted(zz,key = lambda x:sum(int(digit) for digit in str(x)))
print(sortlist2)