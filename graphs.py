import matplotlib.pyplot as plt
from dbQueries import queries
import datetime

class graph:
    def __init__(self):
        self.database = queries()

    def get_profit(self):
        return (self.database.get_TotalRevenue()) - (self.database.get_costOfGoodsSold())

    def show_progress(self):
        x = self.database.get_list_sold()
        plt.plot(x)
        plt.show()
