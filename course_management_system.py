from abc import ABC, abstractmethod
from typing import List

# Course Interface
class Course(ABC):
    @abstractmethod
    def __init__(self, name: str, instructor: 'Professor', content: str):
        pass

    @abstractmethod
    def assign_assignment(self, assignment: 'Assignment'):
        pass

    @abstractmethod
    def view_assignments(self) -> List['Assignment']:
        pass

    @abstractmethod
    def get_instructor(self) -> 'Professor':
        pass

# Assignment Abstract Class
class Assignment(ABC):
    @abstractmethod
    def __init__(self, title: str, description: str):
        pass

    @abstractmethod
    def complete(self):
        pass

# UndergraduateCourse Class
class UndergraduateCourse(Course):
    def __init__(self, name: str, instructor: 'Professor', content: str):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.assignments = []

    def assign_assignment(self, assignment: Assignment):
        self.assignments.append(assignment)

    def view_assignments(self) -> List[Assignment]:
        return self.assignments

    def get_instructor(self) -> 'Professor':
        return self.instructor

# GraduateCourse Class
class GraduateCourse(Course):
    def __init__(self, name: str, instructor: 'Professor', content: str):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.assignments = []

    def assign_assignment(self, assignment: Assignment):
        self.assignments.append(assignment)

    def view_assignments(self) -> List[Assignment]:
        return self.assignments

    def get_instructor(self) -> 'Professor':
        return self.instructor

# Assignment Abstract Class
class Assignment(ABC):
    @abstractmethod
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False

    @abstractmethod
    def complete(self):
        self.completed = True

# Student Class
class Student:
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
                progress[course.name].append((assignment.title, "Completed" if assignment.completed else "Incomplete"))
        return progress

# Professor Class
class Professor:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def create_course(self, name: str, content: str) -> Course:
        return UndergraduateCourse(name, self, content)

# Example Usage
professor = Professor("Dr. Smith", "smith@example.com")
student = Student("Alice", "alice@example.com")

course = professor.create_course("Introduction to Computer Science", "Fundamental concepts of programming")

assignment1 = Assignment("Programming Assignment 1", "Write a program to calculate factorial")
assignment2 = Assignment("Programming Assignment 2", "Write a program to find prime numbers")

course.assign_assignment(assignment1)
course.assign_assignment(assignment2)

student.enroll_course(course)

student.complete_assignment(assignment1)

print("Student progress:")
print(student.view_progress())
