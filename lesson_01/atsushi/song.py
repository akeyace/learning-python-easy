class Song:
    def __init__(self, name, ganre):
        self.name = name
        self.ganre = ganre

    def get(self):
        return self.name + " " + self.ganre
