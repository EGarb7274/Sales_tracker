class watch:
    def __init__(self, name, condition, price_bought, price_sold, date_bought, date_sold):
        self.name = name
        self.condition = condition
        self.priceB = price_bought
        self.priceS = price_sold
        self.dateB = date_bought
        self.dateS = date_sold

    def estimated_profit(self, avgSoldPrice):
        return self.priceB - avgSoldPrice
