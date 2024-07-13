
def a(i,x):
    if i > x:
        return
    print(i,end = " ")
    return a(i+1,x)
x = int(input("Sonni kiriting: "))
a(1,x)