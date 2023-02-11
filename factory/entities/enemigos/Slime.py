
from matplotlib.pyplot import cla
from torch import rand

from AEnemigo import AEnemigo
from random import random


class Slime(AEnemigo):
    
    def __init__(self, nombre, poder) -> None:
        super().__init__(nombre, poder)
        self.drop = "JOYA"
        
    def atacar(self):
        damage = self.poder * random()
        print(f"El Slime ataca e inflinge {damage} puntos de daño")