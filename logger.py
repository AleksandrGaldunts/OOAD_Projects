class User:
    def __init__(self,name:str,age:int,password:str,gender:str,phone_number:int):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.password = password

        if self.is_valid_password():
            print("Good password")
        else:
            print("Bad password")

    def is_valid_password(self):
        if len(self.password)>=8:
            return True
        else:
            return False
class Logger:
    def __init__(self,user):
            if user.is_valid_password():
                print("You can log in")
            # else:
            #     raise ValueError


class EmailNotifier:
    def send_email_notification(self, message):
        print(f"Email Notification: {message}")

class InAppNotifier:
    def send_in_app_notification(self, message):
        print(f"In-App Notification: {message}")

class PushNotifier:
    def send_push_notification(self, message):
        print(f"Push Notification: {message}")

class ProjectManager(Logger,EmailNotifier,InAppNotifier,PushNotifier,User):
    def __init__(self, username):
        super().__init__(username)

class TeamMember(Logger,InAppNotifier,PushNotifier,User):
    def __init__(self, username):
        super().__init__(username)

user = User('Alik',21,'12345678','Male',37498620852)

ob = Logger(user)

print(user.is_valid_password)

# class ExternalContractor(Logger, EmailNotifier, InAppNotifier, PushNotifier, TeamMember, ProjectManager):
#     pass
# Diamond problem karajana ExternalContractor class i jarangman es hertakanutyan jamanak

# ays hertakanutyamn ete jarangumy katarenq arden inheritance i xndir chi arajana
class ExternalContractor(TeamMember, ProjectManager, Logger,EmailNotifier, InAppNotifier, PushNotifier):
    def __init__(self,username):
        super().__init__(username)






















