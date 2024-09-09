from abc import ABC,abstractmethod
class Patient:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
        self.medical_history = []

class Doctor:
    def __init__(self,name:str,contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.appointment_dict = {}

    def manage_appointments(self,patient:Patient,appointment:str):
        if patient.name not in self.appointment_dict:
            self.appointment_dict[patient.name]  = []
        self.appointment_dict[patient.name].append(appointment)


    def manage_patient_information(self,patient:Patient,medical_history:str):
        patient.medical_history.append(medical_history)

class MedicalStaff:
    def __init__(self,name:str,position:str):
        self.name = name
        self.position = position

    def manage_hospital_operations(self):
        return f"{self.name} is managing all operations as his position is {self.position} "


class MedicalOperation(ABC):
    @abstractmethod
    def do_procedure(self):
        ...

class MedicalProcedure(MedicalOperation):
    def __init__(self,procedure_name:str,patient:Patient):
        self.procedure_name = procedure_name
        self.patient = patient

    @abstractmethod
    def do_procedure(self):
        ...

class Surgery(MedicalProcedure):
    def do_procedure(self):
        return f"Doing Surgery named as a {self.procedure_name} to Patient {self.patient.name}"

class CheckUp(MedicalProcedure):
    def do_procedure(self):
        return f"Doing CheckUp named as a {self.procedure_name} to Patient {self.patient.name}"



patient = Patient("Vazgen",58)
doctor = Doctor("Svetlana vasilevna","+37455154829")
doctor.manage_appointments(patient,"handipum aysor")
print(doctor.appointment_dict)

doctor.manage_patient_information(patient,"Vazgeny kolonoskopia aysor")
print(patient.medical_history)

surgery = Surgery("Kolonoskopia",patient)
print(surgery.do_procedure())
chechup = CheckUp("Hertakan",patient)
print(chechup.do_procedure())

















