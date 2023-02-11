from random import random
from enemigos.Esqueleto import Esqueleto
from enemigos.Demonio import Demonio
from enemigos.Slime import Slime


class FactoriaEnemigos:
    
    def __init__(self) -> None:
        pass
    
    
    def makeEnemy(self):
        rng = random() * 100
        if 0 < rng < 35:
            return Esqueleto("Esqueleto", 25)
        if 35 <= rng < 65:
            return Demonio("Demonio Jefe", 30)
        return Slime("Slime verde", 15)