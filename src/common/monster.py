from random import randint
from typing import Optional, cast

from faker import Faker

from .poketype import PokeType
from .waza import waza

fake = Faker()


class Monster:
    def __init__(
        self,
        hp: int = randint(10, 100),
        name: str = cast(str, fake.name()),
        type1: PokeType = PokeType.Normal,
        type2: Optional[PokeType] = None,
        moves: Optional[list[waza]] = None,
    ):
        self.hp = hp
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.moves = moves
