suz = int(input("Sonni kiriting: "))
res = str(suz)
print(type(res))
if res == res[::-1]:
    print("Palindrom")
else:
    print("Palindrom emas")

suz = input("Sozni kiriting: ")
print(suz == suz[::-1])