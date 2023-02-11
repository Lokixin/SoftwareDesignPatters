from abc import ABC
from abc import abstractmethod


class AEnemigo(ABC):
    
    @abstractmethod
    def __init__(self, nombre, poder) -> None:
        self.nombre = nombre
        self.poder = poder
        self.drop = ""
        
        
    @abstractmethod
    def atacar(self):...
    