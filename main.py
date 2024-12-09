from dbQueries import queries
from graphs import graph

if __name__ == "__main__":
    database = queries()
    info = graph()
    #database.del_table("watches")
    database.create_table()
    database.add_entry("Omega Speedmaster 2020", "Excellent", 2200)
    database.get_FullDB()
    database.sell_watch(688204)
    print('sold:')
    database.get_sold()
    #print(f"Total profit ${info.get_profit()}")
    print(f"Total unsold inventory: {database.get_TotalUnSold()}")