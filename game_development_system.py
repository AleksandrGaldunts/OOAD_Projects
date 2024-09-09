from  datetime import datetime
from validators import String,DateTime,Email
from abc import ABC,abstractmethod
class Game(ABC):
    title = String()
    genre = String()
    release_date = DateTime()
    def __init__(self,title:str,genre:str,release_date:datetime):
        self.title = title
        self.release_date = release_date
        self.genre = genre

    @abstractmethod
    def get_info(self):
        ...

class Action(Game):
    def __init__(self,title,genre,release_date,action_type):
        super().__init__(title,genre,release_date)
        self.action_type = action_type

    def get_info(self):
        print(f'Title:{self.title}, Genre:{self.genre},Release_date:{self.release_date},Type:{self.action_type}')

class Strategy(Game):
    def __init__(self,title,genre,release_date,strategy_type):
        super().__init__(title,genre,release_date)
        self.strategy_type = strategy_type

    def get_info(self):
        print(f'Title:{self.title}, Genre:{self.genre},Release_date:{self.release_date},Type:{self.strategy_type}')

class Developer:
    name = String()
    contact_info = Email()
    def __init__(self,name:str,contact_info:Email):
        self.name = name
        self.contact_info = contact_info
        self.games = []

    def create_game(self,game:Game):
        self.games.append(game)

class Publisher:
    name = String()
    contact_info = Email()
    def __init__(self,name:str,contact_info:Email):
        self.name = name
        self.contact_info = contact_info
        self.games = {}

    def release_game(self, game:Game, sales):
        self.games[game.title] = sales

    def list_releases(self):
        for title, sales in self.games.items():
            print(f"Title: {title}, Sales: {sales}")

dev1 = Developer("Alice", "alice@example.com")
dev2 = Developer("Bob", "bob@example.com")

game1 = Action("Action Blast", "Action",datetime(2023, 6, 1), "Shooter")
game2 = Strategy("Strategic Minds", "Strategy",datetime(2023, 7, 15), "Turn-Based")


publisher = Publisher("Ivan","some@mail.ru")

dev1.create_game("game1")
dev1.create_game("game2")

publisher.release_game(game1,20000)
publisher.list_releases()

game1.get_info()















