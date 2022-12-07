import random
class Dice:
    def roll(self):
        fao = random.randint(1,6)
        seco = random.randint(1,6)
        return fao, seco

wee = Dice()
print(wee.roll())

