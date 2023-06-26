from ..randomizer import Randomizer
import random


class Dice(Randomizer):
    def __init__(self, name: str, sides: int = 6):
        super().__init__(name)
        self.sides = sides

    @property
    def has_sub_features(self) -> bool:
        return False

    def randomize(self):
        return random.randint(1, self.sides)
    