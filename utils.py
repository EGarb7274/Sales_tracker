import matplotlib.pyplot as plt
from dbQueries import queries
import sys
import datetime

class utilities:
    def __init__(self):
        self.database = queries()

    def get_profit(self):
        return (self.database.get_TotalRevenue()) - (self.database.get_costOfGoodsSold())

    def show_progress(self):
        x = self.database.get_list_sold()
        plt.plot(x)
        plt.show()

    def masked_inp(self, prompt):
        print(prompt, end='')
        password = ""
        while True:
            char = sys.stdin.read(1)
            if char == '\n':
                break
            password += '*'
            sys.stdout.write('*')
            sys.stdout.flush()
        print()
        return password

