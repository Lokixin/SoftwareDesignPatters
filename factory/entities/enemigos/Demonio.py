from AEnemigo import AEnemigo


class Demonio(AEnemigo):
    
    def __init__(self, nombre, poder) -> None:
        super().__init__(nombre, poder)
        self.drop = "ARMADURA"
    
    def atacar(self):
        pass