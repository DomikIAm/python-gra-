class Enemy:
    def __init__(self, HP, Attack, Mana, Agility, Rage):
        self.HP = HP
        self.Attack = Attack
        self.Mana = Mana
        self.Agility = Agility
        self.HP = HP
        self.Rage = Rage 

Noob = Enemy(5,5,5,5,0)
CentaurousRex = Enemy(10,10,10,10,0)
Common_Mob = Enemy(20,20,20,20,50)
Boss = Enemy(30,30,30,30,100)


class Postac:
    def __init__(self, HP, Attack, Mana, Agility, Rage):
        self.HP = HP
        self.Attack = Attack
        self.Mana = Mana
        self.Agility = Agility
        self.HP = HP
        self.Rage = Rage
 

Basic = Postac(10,10,10,10,0)
Tank = Postac(30,5,0,5,0)
Berserker = Postac(20,10,0,10,100)
Hanger = Postac(15,5,0,20,0)      #wieszak w sensie xd
Assasin = Postac(5,20,5,15,0)
Healer = Postac(10,5,20,5,0)
Tryton = Postac(10,18,0,12,0)
Warrior = Postac(15,15,0,10,0)
God = Postac(99,99,99,99,999)
Loser = Postac(0,0,0,0,0)