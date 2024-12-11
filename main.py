from dbQueries import queries
from utils import utilities
import getpass
from watches import watch
from WebScraper import reddit_scrape

if __name__ == "__main__":

    database = queries()
    info = utilities()
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

    login_info =[]
    if login_info == 0:
        print("Find a watch \n--------------")
        cid = input("Enter your client ID: ")
        cs = input("Enter your client secret: ")
        ua = input("Enter your user agent: ")
        user = input("Enter your username: ")
        password = getpass.getpass("Enter password: ")
        check = input("Would you like to save your login info?")
        if check.lower() == "yes":
            login_info.append(cid,cs,ua,user,password)
        reddit_scrape(cid,cs,ua,user,password)
    else:
        for i in login_info
