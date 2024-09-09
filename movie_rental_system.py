from abc import ABC,abstractmethod
class Movie(ABC):
    def __init__(self,title:str,genre:str,rating:float):
        self.title = title
        self.genre = genre
        self.rating = rating

    @abstractmethod
    def movie_type(self):
        ...

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"

class Drama(Movie):
    def movie_type(self):
        return "Drama"

class Comedy(Movie):
    def movie_type(self):
        return "Comedy"

class RentalOperation(ABC):

    @abstractmethod
    def search_movie(self,movie):
        ...

    @abstractmethod
    def rent_movie(self,movie,duration):
        ...

    @abstractmethod
    def view_rental_history(self):
        ...

    @abstractmethod
    def return_movie(self,movie):
        ...

class Customer(RentalOperation):
    def __init__(self,name:str,contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []
        self.searching_history = []

    def search_movie(self,movie:Movie):
        self.searching_history.append(movie)


    def rent_movie(self,movie:Movie,duration:int):
        self.rental_history.append((movie,duration))
        return f"rented {movie} for {duration} duration"


    def view_rental_history(self):
        return self.rental_history

    def return_movie(self,movie:Movie):
        for rental in self.rental_history:
            if rental[0] == movie:
                self.rental_history.remove(rental)
                return f"Returned {movie.title}"
        return f"{movie.title} not found in rental history"



class Rental(RentalOperation):
    def __init__(self,customer:Customer,movie:Movie,rental_duration:int):
        self.customer = customer
        self.movie = movie
        self.rental_duration = rental_duration

customer = Customer("Alik","098620852")
drama  = Drama("Xose Ignasio","drama",5.0)
comedy = Comedy("xndalu ban","comedy", 5.0)
customer.search_movie(drama)
customer.search_movie(comedy)

for history in customer.searching_history:
    print(history)

print(customer.rent_movie(drama,4))

