import random

x = random.randint(1, 100)

while True:
    y = int(input("Deine Zahl:"))
    if y==x:
        print("Du hast gewonnen!")
        break
    else:
        if y < x:
            print("Die Zahl ist grösser")
        else:
            print("Die Zahl ist kleiner")





