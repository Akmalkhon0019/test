number = [1, 3, 10, 21, 7]
name = ['Kahn', 'Maldini', 'Messi', 'Owen', 'Shevchenko']
country = ['Germaniya', 'Italiya', 'Argentina', 'England', 'Ukrain']
player = {}
for i in range(len(number)):
    player[number[i]] = {name[i]: country[i]}
    
print(player)




