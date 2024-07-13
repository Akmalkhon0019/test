def EKUB(a,b):
    if a == b:
        return a
    if a > b:
        return EKUB(a - b,b)
    else:
        return EKUB(a,b - a)
ls = list(map(int,input("List elementlarini kiriting: ").split()))
mn,mx = min(ls),max(ls)
print(f"EKUB({mx},{mn}) = {EKUB(mn,mx)}")