from model.User import User


class Teacher(User):
    def can_update(self, skill_id: int) -> bool:
        return True

    def __str__(self):
        return f"Teacher {self.name} is number {self.id}"
