from ..feature import Feature


class Randomizer(Feature):
    def __init__(self, name: str):
        super().__init__(name)

    @property
    def is_fungible(self) -> bool:
        return False

    @property
    def has_action(self) -> bool:
        return True

    @property
    def has_sub_features(self) -> bool:
        raise NotImplementedError

    def randomize(self):
        raise NotImplementedError
