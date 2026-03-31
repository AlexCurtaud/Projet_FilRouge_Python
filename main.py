from model.Cohort import Cohort
from model.User import User
from model.Student import Student
from model.Teacher import Teacher


def main():
    print("Hello from projet-filrouge-python!")
    user = User(1, "Booster")
    print(user.name)
    print(user)
    student = Student(2, "Joe", [1, 2, 3, 4])
    print(student.name)
    print(student)
    teacher = Teacher(3, "Bibimbap")
    print(teacher)
    print(student.can_update(5))

    student1 = Student(4, "Bob", [1, 2])
    student2 = Student(5, "Jess", [3, 7])

    cohort1 = Cohort()
    cohort1.add_user(student1)
    cohort1.add_user(student2)
    print(cohort1)

    cohort2 = Cohort()
    cohort2.add_user(student)

    print(cohort2)

    cohort3 = cohort1 + cohort2

    print(cohort3)


if __name__ == "__main__":
    main()
