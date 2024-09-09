from __future__ import annotations
from validators import Email,Integer,String

class Student:
    name = String()
    contact_info = Email()
    def __init__(self,name:str,contact_info:Email):
        self.name = name
        self.contact_info = contact_info

    def __repr__(self):
        return f"Name:{self.name},contact_info:{self.contact_info}"

class Teacher:
    name = String()
    contact_info = Email()
    subject = String()
    def __init__(self,name:str,contact_info:Email,subject:str):
        self.name = name
        self.contact_info = contact_info
        self.subject = subject
        self.courses = []

    def add_subject(self,subject):
        self.courses.append(subject)

    def view_studets_progress(self,student:Student,course:Course):
        if student in course.students:
            print("Students is involved in process")
        else:
            print("not involved in")
    def __repr__(self):
        return f"Name:{self.name},contact_info:{self.contact_info} subject:{self.subject}"

class Course:
    def __init__(self,course_name:str,teacher:Teacher):
        self.name = course_name
        self.teacher = teacher
        self.students = []

    def __repr__(self):
        return f"Coursename:{self.course_name},Teacher:{self.teacher}"

class Math(Course):
    pass

class English(Course):
    pass

student1 = Student("ALik","abc@mail.ru")
student2 = Student("vazgen","abc@mail.ru")

teacher = Teacher("Afo","afo@mail.ru",'Matem')

course = Course("Matem",teacher)
course.students.append(student1)
course.students.append(student2)
teacher.add_subject("Angl")
teacher.add_subject("Matem")
for i in teacher.courses:
    print(i)

for st in course.students:
    print(st)

teacher.view_studets_progress(student1,course)




