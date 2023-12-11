import random
import numpy

acc = 10000

high = 0
opt = -1
for i in range(1, 101):
    tmph = 0
    amph = []

    for x in range(0, acc):
        odds = 10
        rein = i
        money = 2000

        rein = rein / 100

        for c in range(20):
            rand = random.randrange(0, odds, 1)
            if (rand > 0):
                money += money * rein
            else:
                money = (money * (1 - (rein*0.75)))

        if (x<1):
            tmph = money

        if (money < tmph):
            tmph = money

        amph.append(money)

    aver = sum(amph)/len(amph)

    tmph = aver

    if (tmph > high): # Fixed indentation
        high = tmph
        opt = i

print (high)
print("High: $"+str(round(high,2))+", Optimal Percent: "+str(opt)+"%")
