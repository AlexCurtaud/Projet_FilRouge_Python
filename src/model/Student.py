from model.Users import Users


class Student(Users):
    def __init__(
        self,
        user_id: int,
        name: str,
        validated_skill_id: list[int],
    ):
        super().__init__(user_id, name)
        self.__validated_skill_id = validated_skill_id

    def can_update(self, skill_id: int) -> bool:
        for skill in self.__validated_skill_id:
            if skill_id == skill:
                return True
        return False

    def add_validated_skill(self, skill_id: int) -> None:
        for skill in self.__validated_skill_id:
            if skill == skill_id:
                return None
            else:
                self.__validated_skill_id.append(skill_id)
        return None
