import sqlite3
import json
import random

class Functions:
    def get_new_exercise() -> tuple:
        with open("files/pr.json", "r", encoding="utf-8") as file:
            data = list(json.load(file).items())
            amount_true_answers = random.randint(1,4)
            true_answers = [random.choice(data)[0] for i in range(amount_true_answers)]  
            false_answers = [random.choice(random.choice(data)[1]) for i in range(5-amount_true_answers)]  
            result = true_answers.copy() + false_answers.copy()
            random.shuffle(result)
        
            answer = ""
            for i in range(len(result)):
                if result[i] in true_answers:
                    answer += str(i+1)
            return (result, answer)

class BotDB:
    def __init__(self, db_file) -> None:
        self.database = sqlite3.connect(db_file)
        self.cursor = self.database.cursor()

    def close(self):
        self.database.close()