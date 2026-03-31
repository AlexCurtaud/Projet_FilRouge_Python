from dataclasses import dataclass


@dataclass
class Skill:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
