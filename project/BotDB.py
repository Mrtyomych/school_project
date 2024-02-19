import sqlite3

class BotDB:
    def __init__(self, db_file) -> None:
        self.database = sqlite3.connect(db_file)
        self.cursor = self.database.cursor()

    

    def close(self):
        self.database.close()

