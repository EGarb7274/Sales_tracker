from dbQueries import queries
from graphs import graph
from watches import watch

if __name__ == "__main__":
    database = queries()
    info = graph()
    #database.del_table("watches")
    database.create_table()
    database.add_entry_boughtNotSold("Omega Speedmaster 2020", "Excellent", 2200)
    database.add_entry_boughtSold("Tudor Black Bay 58", "Excellent", 2000, 2200)
    database.get_FullDB()
    database.sell_watch(950185, 200000.99)
    print('sold:')
    #print(f"Total profit ${info.get_profit()}")
    print(f"Total profit: {(database.get_TotalRevenue()) - (database.get_costOfGoodsSold())}")
    print(f"sold watches price: {database.get_list_sold()}")
    info.show_progress()