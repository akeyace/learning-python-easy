class Music:
    def __init__(self,songs):
        self.songs = songs

    def get(self):
        result = ()
        for song in self.songs:
            result = result + song.get()

        return result