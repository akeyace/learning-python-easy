class Song:
    def __init__(self, songName, genre):
        self.songName = songName
        self.genre = genre

    def get(self):
        return self.songName.get(), self.genre.get()

