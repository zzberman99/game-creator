class Feature:
    count = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.count
        self.count += 1

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.name}-{self.id}"

    @property
    def is_fungible(self) -> bool:
        raise NotImplementedError

    @property
    def has_action(self) -> bool:
        raise NotImplementedError

    @property
    def has_sub_features(self) -> bool:
        raise NotImplementedError
