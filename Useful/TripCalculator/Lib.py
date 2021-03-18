class location:
    def __init__(self, name):
        self.name = name


class plan:
    def __init__(self, name):
        self.namey = name
        self.lon = location('London')
        self.par = location('Paris')
        self.mad = location('Madrid')
        self.ven = location('Venice')
        self.vie = location('Vienna')
        self.rom = location('Rome')
        self.ath = location('Athens')

    def getPrice(self, loc1, loc2):
        l1 = loc1.name
        l2 = loc2.name
        pric = 0
        if l1 == 'London':
            if l2 == 'Paris':
                pric = 5
            elif l2 == 'Madrid':
                pric = 23
            elif l2 == 'Venice':
                pric = 24
            elif l2 == 'Vienna':
                pric = 33
            elif l2 == 'Rome':
                pric = 26
            elif l2 == 'Athens':
                pric = 25
            else:
                pric = -1
        elif l1 == 'Paris':
            if l2 == 'London':
                pric = 1
            elif l2 == 'Madrid':
                pric = 45
            elif l2 == 'Venice':
                pric = 60
            elif l2 == 'Vienna':
                pric = 40
            elif l2 == 'Rome':
                pric = 22
            elif l2 == 'Athens':
                pric = 120
            else:
                pric = -1
        elif l1 == 'Madrid':
            if l2 == 'Paris':
                pric = 22
            elif l2 == 'London':
                pric = 20
            elif l2 == 'Venice':
                pric = 66
            elif l2 == 'Vienna':
                pric = 42
            elif l2 == 'Rome':
                pric = 24
            elif l2 == 'Athens':
                pric = 100
            else:
                pric = -1
        elif l1 == 'Venice':
            if l2 == 'Paris':
                pric = 51
            elif l2 == 'Madrid':
                pric = 70
            elif l2 == 'London':
                pric = 22
            elif l2 == 'Vienna':
                pric = 115
            elif l2 == 'Rome':
                pric = 57
            elif l2 == 'Athens':
                pric = 100
            else:
                pric = -1
        elif l1 == 'Vienna':
            if l2 == 'Paris':
                pric = 40
            elif l2 == 'Madrid':
                pric = 34
            elif l2 == 'Venice':
                pric = 100
            elif l2 == 'London':
                pric = 30
            elif l2 == 'Rome':
                pric = 27
            elif l2 == 'Athens':
                pric = 53
            else:
                pric = -1
        elif l1 == 'Rome':
            if l2 == 'Paris':
                pric = 22
            elif l2 == 'Madrid':
                pric = 24
            elif l2 == 'Venice':
                pric = 58
            elif l2 == 'Vienna':
                pric = 27
            elif l2 == 'London':
                pric = 24
            elif l2 == 'Athens':
                pric = 36
            else:
                pric = -1
        elif l1 == 'Athens':
            if l2 == 'Paris':
                pric = 70
            elif l2 == 'Madrid':
                pric = 104
            elif l2 == 'Venice':
                pric = 68
            elif l2 == 'Vienna':
                pric = 42
            elif l2 == 'Rome':
                pric = 36
            elif l2 == 'London':
                pric = 22
            else:
                pric = -1
        else:
            pric = -2

        return pric

    def runPlan(self, arr):
        price = 65
        price = price + self.getPrice(arr[0], arr[1])
        price = price + self.getPrice(arr[1], arr[2])
        price = price + self.getPrice(arr[2], arr[3])
        price = price + self.getPrice(arr[3], arr[4])
        price = price + self.getPrice(arr[4], arr[5])
        price = price + self.getPrice(arr[5], arr[6])
        price = price + self.getPrice(arr[6], arr[0])
        return price
