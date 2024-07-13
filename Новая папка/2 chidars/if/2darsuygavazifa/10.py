raqamlar = []
raqam = None

pre_raqam = float('inf')
kam = True
while True:
    raqam = int(input("Son kiriting: "))
    if raqam == 0:
        break
    if raqam >= pre_raqam:
        kam = False
    pre_raqam = raqam
if kam:
    print("Sonlar kamayib borish tartibida kiritilgan")
else:
    print("Sonlar kamayib borish tartibida kiritilmagan")
