def Soat(v):
    hours = v// 3600
    minutes = (v % 3600) // 60
    seconds = v % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
v = int(input("Vaqtni kiriting (sekundlarda): "))
print(Soat(v))