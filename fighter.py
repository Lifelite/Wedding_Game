

class Toon:

    def __init__(self, name, hp, mp, weapon, sp_move):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.weapon = weapon
        self.sp_move = sp_move


class Druid(Toon):

    def __init__(self, name, sp_move="Bear Slam"):
        super().__init__(name, 50, 50, "Staff", sp_move)
        self.name = name
        self.sp_move = sp_move


    def build(self, name, sp_move):
        