from ..feature import Feature


class Resource(Feature):
    def __init__(self, name: str):
        super().__init__(name)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def is_fungible(self) -> bool:
        return True

    @property
    def has_action(self) -> bool:
        raise False

    @property
    def has_sub_features(self) -> bool:
        return False
