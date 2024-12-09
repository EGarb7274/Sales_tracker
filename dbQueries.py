import sqlite3
import random

class queries:
    def __init__(self):
        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()

    def create_table(self):
        with self.con:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS watches (
                    name TEXT,
                    condition TEXT,
                    price DECIMAL,
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    sold BOOLEAN
                )
            """)

    def get_FullDB(self):
        self.cur.execute("SELECT * FROM watches")
        results = self.cur.fetchall()
        for i in results:
            print(i)

    def add_entry(self, name: str, condition: str, price: float):
        while True:
            uid = random.randint(1,999999)
            try:
                self.cur.execute(f"""INSERT INTO watches VALUES ('{name}', '{condition}', {price}, {uid}, {False})""")
                self.con.commit()
                break
            except sqlite3.IntegrityError:
                continue
        self.con.commit()

    def del_entry(self,id):
        self.cur.execute(f"DELETE FROM watches WHERE uid = {id}")

    def del_table(self, name):
        self.cur.execute(f"DROP TABLE {name}")

    def get_sold(self):
        self.cur.execute("SELECT * FROM watches WHERE sold = 1")
        results = self.cur.fetchall()
        for i in results:
            print(i)

    def get_UnSold(self):
        self.cur.execute("SELECT * FROM watches WHERE sold = 0")
        results = self.cur.fetchall()
        for i in results:
            print(i)

    def get_TotalSold(self):
        self.cur.execute("SELECT * FROM watches WHERE sold = 1")
        results = self.cur.fetchall()[0]
        return results

    def get_TotalUnSold(self):
        self.cur.execute("SELECT SUM(price) FROM watches WHERE sold = 0")
        results = self.cur.fetchall()[0]
        print(int(results))
        return results

    def sell_watch(self, id):
        self.cur.execute(f"UPDATE watches SET sold = 1 WHERE uid = {id}")