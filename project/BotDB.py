import sqlite3

class BotDB:
    def __init__(self, db_file) -> None:
        self.database = sqlite3.connect(db_file)
        self.cursor = self.database.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    id TEXT, 
                    number_of_completed_tasks INT, 
                    number_of_correctly_completed_tasks INT, 
                    total_ex4 INT,
                    correct_ex4 INT,
                    total_ex5 INT,
                    correct_ex5 INT,
                    total_ex9 INT,
                    correct_ex9 INT
                    )""")
        self.database.commit()

    def add_new_user(self, user_id):
        if self.cursor.execute("SELECT id FROM users WHERE id = {}".format(user_id)).fetchone() is None:
            self.cursor.execute(f"INSERT INTO users VALUES ('{user_id}', 0, 0, 0, 0, 0, 0, 0, 0)")
        self.database.commit()

    def return_user_info(self, user_id):
        data = self.cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id)).fetchone()
        self.database.commit()
        return data
    
    def update_database(self, user_id, ex, t_ex, is_correct):
        total, current_ex, t_current_ex = self.cursor.execute("""SELECT number_of_completed_tasks, {}, {} FROM users WHERE id = {}""".format(ex,t_ex, user_id)).fetchone()
        if is_correct:
            total+=1
            current_ex+=1
            t_current_ex+=1
            self.cursor.execute("UPDATE users SET number_of_completed_tasks = {}, {} = {}, {} = {}  WHERE id = {}".format(total, ex, current_ex, t_ex, t_current_ex, user_id))
        else:
            total+=1
            t_current_ex+=1
            self.cursor.execute("UPDATE users SET number_of_completed_tasks = {}, {} = {}  WHERE id = {}".format(total, t_ex, t_current_ex, user_id))
        self.database.commit()





