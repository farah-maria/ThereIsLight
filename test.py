import random


class Enemy:
    """ Enemy who reduces player's power through the game """
    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit 
        self.calories_to_burn = calories_to_burn


Kavanaugh = Enemy("Kavanaugh", 60, 3000)
Schlafly = Enemy("Schlafly", 100, 2000)
Trump = Enemy("Trump", 70, 3500)


def Opponent_Select():
    opp_list = ['Kavanaugh', 'Schlafly', 'Trump']
    rand = random.randint(0, 2)
    opponent = opp_list[rand]
    print(opponent)


Opponent_Select()
