sch = []
son = None
while True:
    son = int(input("Son kiriting: "))
    if son == 0:
        break
    sch.append(son)
son2 = False 
for i in range(1, len(sch)):
    if sch[i] > 0 and sch[i - 1] > 0:
        son2 = True
        break
if son2:
    print("Kamida ikkita qo'shni musbat son kiritilgan.")
else:
    print("Kamida ikkita qo'shni musbat son kiritilmagan.")