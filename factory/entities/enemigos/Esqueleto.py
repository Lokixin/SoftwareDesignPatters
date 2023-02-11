from AEnemigo import AEnemigo


class Esqueleto(AEnemigo):
    
    def __init__(self, nombre, poder) -> None:
        super().__init__(nombre, poder)
        self.drop = "ARMA"
        
        
    def atacar(self):
        pass