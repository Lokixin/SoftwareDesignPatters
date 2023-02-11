from enum import Enum

from entities.enemigos import AbstractEnemy, Skeleton, Slime, Spyder


class Enemigos(Enum):
    SKELETON = 1
    SLIME = 2
    SPYDER = 3
    

class EnemyFactory:
    def __init__(self) -> None:
        self.classes = {
            Enemigos.SKELETON.value: Skeleton,
            Enemigos.SLIME.value: Slime,
            Enemigos.SPYDER.value: Spyder,
        }

    def make_enemy(self, enemy_type: str, **kwargs) -> AbstractEnemy:
        ClaseEnemigo = self.classes[enemy_type]
        return ClaseEnemigo(**kwargs)
