import datetime

from skola import Student, Course
import pytest


@pytest.fixture
def student():
    return Student("Studenten", "Svensson", 34)


@pytest.fixture
def course():
    return Course(1, "Programmering pvt21", datetime.date(2021, 9, 13), datetime.date(2021, 12, 17))


def test_student_enrolment(student, course):
    student.take_course(course)
    assert student in course


def test_student_disenrolment(student, course):
    student.take_course(course)
    student.drop_course(course)
    assert student not in course, f"{str(student)} in course {course}"