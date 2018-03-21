class Song:
    def __init__(self, song_name, genre):
        self.song_name = song_name
        self.genre  = genre

    def get(self):
        return self.song_name.get(), self.genre.get()
