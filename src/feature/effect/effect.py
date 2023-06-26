from ..feature import Feature


class Effect(Feature):
    def __init__(self, name: str, effect_type: str):
        super().__init__(name)
        assert effect_type in {"instant", "periodic", "constant"}
        self.effect_type = effect_type

    @property
    def is_fungible(self) -> bool:
        return False

    @property
    def has_action(self) -> bool:
        return True

    @property
    def has_sub_features(self) -> bool:
        raise NotImplementedError

    def activate(self):
        raise NotImplementedError
