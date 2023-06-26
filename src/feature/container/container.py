from ..feature import Feature


class Container(Feature):
    def __init__(self, name: str):
        super().__init__(name)

    @property
    def is_fungible(self) -> bool:
        return False

    @property
    def has_action(self) -> bool:
        raise NotImplementedError

    @property
    def has_sub_features(self) -> bool:
        return True
