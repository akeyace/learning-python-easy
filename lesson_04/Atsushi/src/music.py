class Music:
    def __init__(self, songs):
        self.songs = songs

    def get(self):
        result = {}
        for i, song in enumerate(self.songs):
            result[i] = song.get()
            sorted(result, key=lambda x: ["ジャンル"])

        return result
