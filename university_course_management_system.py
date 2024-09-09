from abc import ABC,abstractmethod
class StringValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, '')

    def __set__(self, instance, value):
        if instance is None:
            return self
        if not isinstance(value, str):
            raise TypeError(f"must be a string")
        instance.__dict__[self.name] = value


class Assignment(ABC):
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False

    @abstractmethod
    def complete(self):
        ...

class Course(ABC):

    name = StringValue()
    content = StringValue()
    instructor = StringValue()

    def __init__(self,name,instructor,content):
        self.name = name
        self.content = content
        self.instructor = instructor

    @abstractmethod
    def assign_assignment(self, assignment):
        ...

    @abstractmethod
    def view_assignments(self):
        ...

    @abstractmethod
    def get_instructor(self):
        ...

class UndergraduateCourse(Course):

    def __init__(self, name: str, instructor, content: str):
        super().__init__(name,instructor,content)
        self.assignments = []

    def assign_assignment(self, assignment: Assignment):
        self.assignments.append(assignment)

    def view_assignments(self):
        return self.assignments

    def get_instructor(self):
       return self.instructor


class GraduateCourse(Course):

    def __init__(self, name: str, instructor: 'Professor', content: str):
        super().__init__(name,instructor,content)
        self.assignments = []

    def assign_assignment(self, assignment: Assignment):
        self.assignments.append(assignment)

    def view_assignments(self):
        return self.assignments

    def get_instructor(self):
        return self.instructor

class Student:
    name = StringValue()
    contact_info = StringValue()

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.enrolled_courses = []

    def enroll_course(self, course: Course):
        self.enrolled_courses.append(course)

    def complete_assignment(self, assignment: Assignment):
        assignment.complete()

    def view_progress(self):
        progress = {}
        for course in self.enrolled_courses:
            progress[course.name] = []
            for assignment in course.view_assignments():
                progress[course.name].append((assignment.title, "Completed" if assignment.completed else "uncomplete"))
        return progress

class Professor:

    name = StringValue()
    contact_info = StringValue()

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info




professor = Professor("John", "043559986")
student = Student("Alik", "098620852")
assignment = Assignment("OOP","Do all tasks")
graduated = GraduateCourse("12b",professor,"Avartakan")
print(graduated.assign_assignment("handznararutyun"))
print(graduated.view_assignments())





