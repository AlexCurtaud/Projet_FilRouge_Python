from dataclasses import dataclass
from typing import Optional


@dataclass
class Validation:
    skill_id: int
    status: str
    pre_validated_by: str
    teacher_id: Optional[int] = None

    def __str__(self) -> str:
        if self.teacher_id is None:
            return f"Skill {self.skill_id} {self.status} by {self.pre_validated_by}"
        return f"Teacher {self.teacher_id} {self.status} skill {self.skill_id} of {self.pre_validated_by}"
