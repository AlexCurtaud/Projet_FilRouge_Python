from model.Cohort import Cohort
from model.Skill import Skill
from model.Student import Student
from model.Teacher import Teacher
from model.Validation import Validation


def main() -> None:
    student = Student(2, "Joe", [1, 3, 4])
    student1 = Student(4, "Bob", [1, 2])
    student2 = Student(5, "Jess", [3, 4])
    teacher = Teacher(3, "Bibimbap")

    cohort1 = Cohort()
    cohort1.add_user(student1)
    cohort1.add_user(student2)
    cohort2 = Cohort()
    cohort2.add_user(student)
    cohort3 = cohort1 + cohort2

    java = Skill(1, "Java")
    data_base = Skill(2, "Data Base")
    python = Skill(3, "Python")
    javascript = Skill(4, "JavaScript")

    validation1 = Validation(
        skill_id=java.id, status="pre validated", pre_validated_by=student.name
    )
    validation2 = Validation(
        skill_id=python.id,
        status="validated",
        pre_validated_by=student.name,
        teacher_id=teacher.id,
    )

    print(data_base)
    print(javascript)
    print(validation1)
    print(validation2)


if __name__ == "__main__":
    main()
