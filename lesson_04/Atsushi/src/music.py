from operator import itemgetter

class Music:
    def __init__(self, songs):
        self.songs = songs

    def get(self):
        result = ()
        for song in self.songs:
            result = result + song.get()
            result.sorted(result, key=itemgetter(1))

        return result
