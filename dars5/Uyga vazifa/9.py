def yevrey(x, y):
    return y, x
x = float(input("Haqiqiy sonni kiriting <misol: 12.12>: ")) 
y = float(input("Huddi shunday yana haqiqiy sonni kiriting: "))
x, y = yevrey(x, y)
print(f"x={x}, y={y}")