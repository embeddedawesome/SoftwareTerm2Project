import pickle

class DnDCharacterDatabase:
    def __init__(self, filename: str):
        self.filename = filename
        self.characters = []
        self.load()

    def load(self, filename: str = None):
        try:
            with open(self.filename if not filename else filename, "rb") as file:
                self.characters = pickle.load(file)
        except:
            return

    def save(self, filename: str = None):
        with open(self.filename if not filename else filename, "wb") as file:
            pickle.dump(self.characters, file, pickle.HIGHEST_PROTOCOL)

    def reset(self):
        self.characters = []

