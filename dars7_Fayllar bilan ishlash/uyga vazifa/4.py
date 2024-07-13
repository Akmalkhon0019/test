import random
def tls():
    ls = [random.randint(1, 1000000) for _ in range(1000)]
    N = random.randint(0, 999)
    return ls, N
def tubmi(son):
    if son < 2:
        return False
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            return False
    return True
def tub_sonlar(ls, N):
    tub_sonlar = [son for son in ls[N+1:] if tubmi(son)]
    return tub_sonlar
ls, N = tls()
print("Tasodifiy ro'yxat:", sorted(ls))
print(f"Tasodifiy tanlangan N: {N}")
print("N dan keyingi tub sonlar:", sorted(tub_sonlar(ls, N)))
