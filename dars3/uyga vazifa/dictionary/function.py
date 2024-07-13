def juft_sonmi(x):
    return x % 2 == 0

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar = filter(juft_sonmi, sonlar)

print(list(juft_sonlar))  # [2, 4, 6]
