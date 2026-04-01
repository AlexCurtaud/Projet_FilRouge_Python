class Users:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def can_update(self, skill_id: int) -> bool:
        return False

    def __str__(self) -> str:
        return f"{self.name} is number {self.id}"
