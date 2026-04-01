from typing import List
from model.Users import Users


class Cohort:
    def __init__(self, user_list: List[Users] | None = None):
        if user_list is None:
            user_list = []
        self.__user_list: List[Users] = user_list

    def add_user(self, student: Users) -> None:
        for user in self.__user_list:
            if user == student:
                return None
        self.__user_list.append(student)
        return None

    def __add__(self, other: "Cohort") -> "Cohort":
        return Cohort(self.__user_list + other.__user_list)

    def __str__(self) -> str:
        tab = []
        for student in self.__user_list:
            tab.append(student.name)
        return f"{' '.join(tab)}"
