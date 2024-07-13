import random

def ls_yaratish():
    ls = [random.randint(100, 1000) for _ in range(100)]
    N = random.randint(1, 100)
    return ls, N
def juft_sonlar(ls, N):
    juft_sonlar = [son for son in ls[:N] if son % 2 == 0]
    return juft_sonlar
ls, N = ls_yaratish()
print("Tasodifiy ro'yxat:", sorted(ls))
print(f"Tasodifiy tanlangan N: {N}")
print("N gacha bo'lgan juft sonlar:", sorted(juft_sonlar(ls, N)))