import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def classroom():
    teacher = Teacher("Severus Snape")
    students = [Student(f"Student{i}") for i in range(9)]
    course_title = "Potions"
    return Classroom(teacher, students, course_title)

def test_add_student(classroom):
    print(len(classroom.students))
    new_student = Student("Hermione Granger")
    classroom.add_student(new_student)
    assert len(classroom.students) == 10
    assert new_student in classroom.students
    assert True

def test_add_too_many_students(classroom):
    with pytest.raises(TooManyStudents):
        for i in range(3):
            classroom.add_student(Student(f"ExtraStudent{i}"))

def test_remove_student(classroom):
    student_name = classroom.students[0].name
    classroom.remover_student(student_name)
    assert len(classroom.students) == 8
    assert all(student.name != student_name for student in classroom.students)

def test_change_teacher(classroom):
    new_teacher = Teacher("Minerva McGonagall")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher

# Using pytest and the functions that come from it. Such as fixtures, parametrize, raises and mark, where
# ever necessary. Test the following code and theme it after Harry Potter:
