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
                    priceB DECIMAL,
                    priceS DECIMAL,
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    sold BOOLEAN
                )
            """)

    def get_FullDB(self):
        self.cur.execute("SELECT * FROM watches")
        results = self.cur.fetchall()
        for i in results:
            print(i)

    def add_entry_boughtNotSold(self, name: str, condition: str, priceB: float):
        while True:
            uid = random.randint(1,999999)
            try:
                self.cur.execute(f"""INSERT INTO watches VALUES ('{name}', '{condition}', {priceB}, 0, {uid}, {False})""")
                self.con.commit()
                break
            except sqlite3.IntegrityError:
                continue
        self.con.commit()

    def add_entry_boughtSold(self, name: str, condition: str, priceB: float, priceS: float):
        while True:
            uid = random.randint(1,999999)
            try:
                self.cur.execute(f"""INSERT INTO watches VALUES ('{name}', '{condition}', {priceB}, {priceS}, {uid}, {True})""")
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

    def get_TotalRevenue(self):
        self.cur.execute("SELECT SUM(priceS) FROM watches WHERE sold = 1")
        results = self.cur.fetchone()[0]
        return results

    def get_costOfGoodsSold(self):
        self.cur.execute("SELECT SUM(priceB) FROM watches")
        results = self.cur.fetchone()[0]
        return results

    def sell_watch(self, id, priceS):
        self.cur.execute(f"UPDATE watches SET sold = 1, priceS = {priceS} WHERE uid = {id}")

    def get_list_sold(self):
        sold_prices = []
        self.cur.execute("SELECT priceS from watches WHERE priceS > 0")
        results = self.cur.fetchall()
        for i in results:
            sold_prices.append(float(i[0]))
        return sold_prices