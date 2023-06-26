from ..container import Container
from ...resource.resource import Resource
from typing import Union


class Bank(Container):
    def __init__(self, name: str, resource_types: Union[list[Resource], dict[Resource:int]]):
        super().__init__(name)
        self.bank = {}
        if type(resource_types) == list:
            for r in resource_types:
                assert isinstance(r, Resource)
                self.bank[r] = 0
        elif type(resource_types) == dict:
            for r, v in resource_types.items():
                assert isinstance(r, Resource)
                assert type(v) == int
                self.bank[r] = v
        else:
            raise ValueError()

    @property
    def has_action(self) -> bool:
        return False

    def insert(self, r: Resource, v: int = 1):
        self.bank[r] += v

    def remove(self, r: Resource, v: int = 1):
        self.bank[r] -= v
