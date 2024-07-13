n = int(input("C>: "))
a = float(input("Sonni kiriting: "))
if a < 0:
    tip = True
else:
    tip = False
    n -= 1
while n > 0:
    a = float(input("Sonni kiriting: "))
    if (a < 0 and tip == False):
        tip = True
    elif (a > 0 and tip == True):
        tip = False
    else:
        break
    n -= 1
print(n == 0)
