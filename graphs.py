import matplotlib
from dbQueries import queries

class graph:
    def __init__(self):
        self.database = queries()

    def get_profit(self):
        unsold = self.database.get_TotalUnSold()
        sold = self.database.get_TotalSold()
        return sold - unsold