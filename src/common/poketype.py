from enum import Enum, auto


class PokeType(Enum):
    Normal = auto()


poketype_relations = {PokeType.Normal: {PokeType.Normal: 1}}
