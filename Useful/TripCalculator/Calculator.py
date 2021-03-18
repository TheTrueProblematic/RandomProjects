from Useful.TripCalculator.Lib import location, plan
import random

lon = location('London')
par = location('Paris')
mad = location('Madrid')
ven = location('Venice')
vie = location('Vienna')
rom = location('Rome')
ath = location('Athens')

locations = [lon, par, mad, ven, vie, rom, ath]
order = 'hmm'
finPrice = 100000

for c in range(100000):
        random.shuffle(locations)
        strin = 'ORDER: ' + locations[0].name + ", " + locations[1].name + ", " + locations[2].name + ", " + locations[3].name + ", " + locations[4].name + ", " + locations[5].name + ", " + locations[6].name
        plon = plan('test')
        price = plon.runPlan(locations)

        if (price<finPrice) and (price>290):
                order = strin
                finPrice = price

order = order+'\n\n And it costs: $'+str(finPrice)

print(order)