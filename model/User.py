class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def can_update(self, skill_id: int) -> bool:
        return False

    def __str__(self):
        return f"{self.name} is number {self.id}"
