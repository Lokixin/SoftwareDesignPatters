from random import randint

from fabrication.factories import EnemyFactory, Enemigos


if __name__ == "__main__":
    enemy_factory = EnemyFactory()

    for enemy_type in list(Enemigos):
        enemy = enemy_factory.make_enemy(
            enemy_type.value,
            nivel=randint(1, 10),
            vida=randint(50, 100),
            ataque=randint(20, 50),
        )
        print(enemy, end="\n")
        enemy.attack()
