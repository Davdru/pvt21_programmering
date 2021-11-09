import datetime


class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}år"


class Student(Person):
    first_name: str
    last_name: str
    age: int
    courses: list

    def __init__(self, f_name, l_name, a):
        super().__init__(f_name, l_name, a)
        self.courses = []

    def greet(self):
        print(f"Hej jag heter {self.first_name}, id är {id(self)}")

    def take_course(self, course):
        course.enrol(self)
        self.courses.append(course)

    def drop_course(self, course):
        course.disenrol(self)
        self.courses.remove(course)


class Teacher(Person):
    first_name: str
    last_name: str
    age: int
    email: str
    phone_no: str

    def __init__(self, first_name, last_name, age, email, phone_no):
        super().__init__(first_name, last_name, age)
        self.email = email
        self.phone_no = phone_no

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}år\n" \
               f"epost: {self.email}\n" \
               f"phone: {self.phone_no}"

#               Person
#               /   \
#              /     \
#             /       \
#         Student    Teacher
#
# Student och Teacher ärver båda från Person
# Det skall läsas som att en Student är också en person
# samma sak gäller för Teacher


class Course:
    id_: int
    course_name: str
    start_date: datetime.date
    end_date: datetime.date
    students: list[Student]
    teachers: list[Teacher]

    def __init__(self, id_, course_name, start_date, end_date):
        self.id_ = id_
        self.course_name = course_name
        self.start_date = start_date
        self.end_date = end_date
        self.students = []
        self.teachers = []

    def enrol(self, student: Student):
        self.students.append(student)

    def disenrol(self, student: Student):
        self.students.remove(student)

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, teacher: Teacher):
        self.teachers.remove(teacher)

    def __str__(self):
        teachers = '\n'.join(map(str, self.teachers))
        students = '\n'.join(map(str, self.students))
        return f"{self.course_name} {self.start_date} - {self.end_date}\n" \
               f"taught by {teachers}, " \
               f"\nstudents attending:\n{students}"

    def __contains__(self, item):
        return item in self.students


# Hur kan en klass som representerar kurser se ut

if __name__ == '__main__':
    programmering_pvt21 = Course(1, "Programmering", datetime.date(2021, 9, 13), datetime.date(2021, 12, 17))
    databasteknik_pvt21 = Course(2, "Databasteknik", datetime.date(2022, 1, 15), datetime.date(2022, 3, 10))

    student1 = Student("Kalle", "Efternamnsson", 30)
    student2 = Student("Sune", "Ny student", 25)
    student3 = Student("Lisa", "Svensson", 31)
    teacher = Teacher("Björn", "Kjellgren", 40, "bjorn.kjellgren@kyh.se", "192834719845")


    student1.take_course(programmering_pvt21)

    student2.take_course(programmering_pvt21)
    student2.take_course(databasteknik_pvt21)

    student3.take_course(programmering_pvt21)
    student3.take_course(databasteknik_pvt21)

    student3.drop_course(databasteknik_pvt21)
    student3.drop_course(programmering_pvt21)
    print(programmering_pvt21)
    print("-"*100)
    print(databasteknik_pvt21)
    print("-" * 100)
    courses = [programmering_pvt21, databasteknik_pvt21]
    students = [student1, student2, student3]
    # För varje student, hitta alla kurser den läser


    for student in students:
        print(f"{student.first_name} {student.last_name} läser:")
        for course in student.courses:
            print(f"{course.course_name}")
        print("-" * 100)


    print(student3 in programmering_pvt21)