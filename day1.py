from math import *

def Give_input():
    while True:
        x=input("Give mass of vechicle=")
        if x.isnumeric():
            break
        print("Wrong input try again ")
    return x

def Fuelrequired(k):
    o=int(k)
    o=round(o/3)
    o+=2
    return o

fr=Give_input()
print(Fuelrequired(fr))


