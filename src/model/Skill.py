from dataclasses import dataclass


@dataclass
class Skill:
    id: int
    name: str

    def __str__(self) -> str:
        return f"Skill: {self.name} - id: {self.id}"
