from abc import ABC,abstractmethod
class Song:
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length

    def play(self):
        print(f"Playing {self.title} by {self.artist}")

    def get_info(self):
        return f"Title: {self.title}, Artist: {self.artist}, Length: {self.length}"

class Album:
    def __init__(self, title, artist, release_date):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_info(self):
        return f"Album: {self.title}, Artist: {self.artist}, Release Date: {self.release_date}"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def get_info(self):
        return f"Playlist: {self.name}"


class MusicOperation(ABC):
    @abstractmethod
    def search(self, query):
        pass

    @abstractmethod
    def play(self):
        pass

class User:
    def __init__(self, name):
        self.name = name
        self.listening_history = []
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def view_history(self):
        return [song.get_info() for song in self.listening_history]

    def listen(self, song):
        self.listening_history.append(song)
        song.play()

song1 = Song("Snowman", "Sia", "3:30")
song2 = Song("Diamonds", "Rihanna", "4:00")
song3 = Song("Illusion", "Dua Lipa", "2:45")

album = Album("Album one", "Artist A", "2024-01-01")
album.add_song(song1)
album.add_song(song2)

user = User("Alik")


playlist = user.create_playlist("My Favorites")
playlist.add_song(song1)
playlist.add_song(song3)

user.listen(song2)
print(playlist.get_info())
print(user.view_history())




