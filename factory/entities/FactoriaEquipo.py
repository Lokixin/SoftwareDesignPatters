from io import UnsupportedOperation
from equipo.Arma import Arma
from equipo.Arma import Armadura
from equipo.Arma import Joya


class FactoriaEquipo:
    def __init__(self) -> None:
        pass
    
    def makeEquipo(tipo):
        if tipo == "ARMA":
            return Arma()
        
        if tipo == "ARMADURA":
            return Armadura()
        
        if tipo == "JOYA":
            return Joya()
        
        raise UnsupportedOperation(f"El tipo de equipo: {tipo} no se puede crear")