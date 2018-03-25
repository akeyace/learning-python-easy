class Genre:
    def __init__(self, name):
        self.genre = name

    def get(self):
        return "ジャンル: " + self.name.get()