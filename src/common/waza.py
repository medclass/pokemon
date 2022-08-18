from random import randrange

from faker import Faker

from .poketype import PokeType

fake = Faker()


class waza:
    def __init__(
        self,
        name: str = fake.name(),
        type: PokeType = PokeType.Normal,
        attack: int = randrange(10, 101, 5),
    ):
        self.name = name
        self.type = type
        self.attack = attack
