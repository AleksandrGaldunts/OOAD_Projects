# Single responsibility Principe
"""
    Class֊ը պետք է ունենա մեկ և միայն մեկ պատճառ փոխվելու համար։
    Այն իմաստով, թր class֊ը պետք է լինի պատասխանատու միայն մեկ բանի համար։
    Class֊ը պետք է ունենալ միայն մեկ actor
"""
class Task:
    def __init__(self, description: str):
        self.description = description
    def save(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self.description)
    def print(self):
        print(f"Task: {self.description}")
"""
   Սխալ է քանի որ Task class֊ը ունի մի քանի ֆունկցիոնալություն, որն էլ կոտրում է մեր կոդի ճկունությունը,
    այսինքն հետագայում ընդլայնելու համար պետք է վերասահմանենք մեր ամբողջ class-ը, 
    ոչ թե կոդի այն կտորը, որը պատասխանատու է ընդլայման համար։ 
"""
class Task:
    def __init__(self, description: str):
        self.description = description
class TaskSaver:
    def save(self, task: Task, filename: str):
        with open(filename, 'w') as file:
            file.write(task.description)
class TaskPrinter:
    def print(self, task: Task):
        print(f"Task: {task.description}")



