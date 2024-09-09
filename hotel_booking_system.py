from abc import ABC,abstractmethod
from datetime import datetime

class Rooms(ABC):
    def __init__(self,room_number:int, price:int,amenities:list):
        self.room_number = room_number
        self.price = price
        self.amenities = amenities
        self.is_reserved = False

class StandartRoom(Rooms):
    def __init__(self,room_number:int, price:int,amenities:bool):
        super().__init__(room_number,price,amenities)

class DeluxeRoom(Rooms):
    def __init__(self,room_number:int, price:int,amenities:bool):
        super().__init__(room_number,price,amenities)
class Guests:
    def __init__(self,name:str,contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.reservation_history = []

    def search_rooms(self, rooms):
        return [room for room in rooms if not room.is_reserved]

    def book_room(self, rooms, room_number, start_date, end_date):
        available_rooms = self.search_rooms(rooms)
        for room in available_rooms:
            if room.room_number == room_number:
                reservation = Reservations(self, room, start_date, end_date)
                self.reservation_history.append(reservation)
                return reservation
        return None

    def view_reservation_history(self):
        return self.reservation_history

    def leave_feedback(self, reservation, feedback):
        reservation.feedback = feedback

class Reservations(ABC):
    def __init__(self,guest:Guests,room:Rooms,start_date:datetime,end_date:datetime):
        self.guest = guest
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.feedback = None
        self.total_price = self.calculate_total_price()
        room.is_reserved = True

    def calculate_total_price(self):
        number_of_days = (self.end_date - self.start_date).days
        return number_of_days * self.room.price

    def __str__(self):
        return f"Reservation for {self.guest.name} in Room {self.room.room_number} from {self.start_date} to {self.end_date}. Total price: {self.total_price}$"

rooms = [
        StandartRoom(101, 100, ["WiFi", "TV"]),
        DeluxeRoom(201, 200, ["WiFi", "TV", "Mini Bar"]),
    ]


guest1 = Guests("Valeri", "086620852")
available_rooms = guest1.search_rooms(rooms)
start_date = datetime(2024, 6, 1)
end_date = datetime(2024, 6, 5)
reservation1 = guest1.book_room(rooms, 104, start_date, end_date)

