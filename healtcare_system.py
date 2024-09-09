from __future__ import annotations
from validators import Email,Integer,String,DateTime
from datetime import datetime
from abc import ABC,abstractmethod

class abstract(ABC):

    @abstractmethod
    def view_medical_history(self):
        ...

class Patient(abstract):
    name = String()
    contact_info = Email()
    def __init__(self,name:str,contact_info:Email):
        self.name = name
        self.contact_info = contact_info
        self.medical_history = []

    def schedule_appointment(self,doctor:Doctor,appointment:Appointments):
        if appointment not in doctor.appointments:
            doctor.appointments.append(appointment)
        else:
            print("there is no time")

    def view_medical_history(self):
        print("Patient is viewing medical history")

    def __repr__(self):
         return f"Name:{self.name},contact_info:{self.contact_info}"

class Doctor(abstract):
    name = String()
    contact_info = Email()
    speciality = String()
    def __init__(self,name:str,contact_info:Email,speciality:str):
        self.name = name
        self.contact_info = contact_info
        self.speciality = speciality
        self.appointments = []


    def change_appointment_time(self,appointment:Appointments,doctor,patient):
        if appointment in self.appointments:
            self.appointments.remove(appointment)
            self.appointment.append(Appointments(patient,doctor,datetime.now()))

    def view_medical_history(self,patient:Patient):
        print(f"viewing {patient} patients medical history by doctor ")

    def __repr__(self):
        return f"Name:{self.name},contact_info:{self.contact_info},speciality:{self.speciality}"


class Appointments:
    appointment_time = DateTime()
    def __init__(self,patient:Patient,doctor:Doctor,appointment_time:datetime):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Patient:{self.patient}, Doctor:{self.doctor}, appointment_time:{self.appointment_time}"

class InPerson(Appointments):
    pass

class Virtual(Appointments):
    pass

patient = Patient("vazgen","vazgen@mail.ru")
doctor = Doctor("vasilev","vasilev@mail.ru","endokrinolog")
appointment = Appointments(patient,doctor,datetime.now())

patient.schedule_appointment(doctor,appointment)
print(doctor.appointments)

