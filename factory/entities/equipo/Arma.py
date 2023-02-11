from AEquipo import AEquipo
from random import random


class Arma(AEquipo):
    
    def __init__(self) -> None:
        self.poder = 1/(50-20)*random()*100
        print("Enhorabuena, has conseguido un arma")
        
        
    def usar(self, portador):
        print(f"{portador.nombre} ha usado un arma para inflingir {self.poder + 0.2*self.portador.poder} puntos de daño")