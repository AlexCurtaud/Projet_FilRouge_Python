from model.Users import Users


class Teacher(Users):
    def can_update(self, skill_id: int) -> bool:
        return True

    def __str__(self) -> str:
        return f"Teacher {self.name} is number {self.id}"
