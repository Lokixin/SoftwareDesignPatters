from abc import ABC, abstractmethod

from utils import generate_name


class AbstractEnemy(ABC):
    @abstractmethod
    def __init__(self, nivel, vida, ataque) -> None:
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque

    @abstractmethod
    def attack(self) -> None:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        return generate_name()

    def __repr__(self) -> str:
        return f"ENEMIGO:\n{self.name=}\n{self.vida=}\n{self.nivel=}\n{self.ataque=}"


class Slime(AbstractEnemy):
    def __init__(self, nivel, vida, ataque):
        super().__init__(nivel, vida, ataque)

    def attack(self):
        print(f"Slime {self.name} enemigo inflinge {self.ataque} puntos de daño")


class Spyder(AbstractEnemy):
    def __init__(self, nivel, vida, ataque):
        super().__init__(nivel, vida, ataque)

    def attack(self):
        print(f"Spyder {self.name} enemigo inflinge{self.ataque} puntos de daño")


class Skeleton(AbstractEnemy):
    def __init__(self, nivel, vida, ataque):
        super().__init__(nivel, vida, ataque)

    def attack(self):
        print(f"Skeleton {self.name} enemigo inflinge {self.ataque} puntos de daño")
