import os
os.system("clear")
import random as rd

ls = [rd.randint(10,100) for x in range(int(input("n <:)c> ")))]
toq = list(filter(lambda x: x % 2 == 1,ls))


