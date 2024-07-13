# filename = input("Fayl k-ng:>  ")
# with open(filename,"wt") as f:
#     f.write("Hello, World!")
#     print("Fayl yaradildi!")
#     f.seek(0)

fileName =input("Fayl nomi va formatini kiriting >>: ")
text = input("Fayl ichiga matn yozing: >:) ")

try:
    with open(fileName) as file:
        file.write(text)
except FileNotFoundError:
    print("Xato!")
else:
    print(f"{fileName} fayl yaradildi!")
finally:
    print("Dastur yakunlandi!")
