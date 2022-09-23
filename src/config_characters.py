"""Bring all the functions using through all modules"""
import config_system as CS
import config_functions as CF


class Venue:
    """container for infos such as money, level, days menu and price etc"""
    def __init__(self):
        self.level = 1
        self.budgets = 10000
        self.budgets_yesterday = self.budgets
        self.days = 1
        self.wastage = 0
        self.list_foods = [ # More same names mean more preferences
            "Beef burger", "Beef burger", "Beef burger",
            "Fish & chips", "Fish & chips",
            "Pizza", "Pizza"]
        self.list_drinks = [
            "Soft drink", "Soft drink", "Soft drink",
            "Coffee", "Coffee",
            "Beer"]
        self.current_stocks = {
            "Beef burger" : 150,
            "Fish & chips" : 100,
            "Pizza" : 100,
            "Soft drink" : 170,
            "Coffee" : 120,
            "Beer" : 60 }
        self.yesterday_stocks = {}
        self.stock_prices = {
            "Beef burger" : 15,
            "Fish & chips" : 15,
            "Pizza" : 13,
            "Soft drink" : 4,
            "Coffee" : 5,
            "Beer" : 10 }
        self.supplier_prices = {
            "Beef burger" : 7,
            "Fish & chips" : 6,
            "Pizza" : 5,
            "Soft drink" : 2,
            "Coffee" : 3,
            "Beer" : 5 }
        self.daily_staffs_wage = 1500
        self.difficulty = 1
        self.price_adj = 1

    def days_addup(self):
        """day counts and control level of difficulty in game after every round"""
        self.days += 1
        self.difficulty = 1 + (self.days-1) * 0.1

    def opening_venue(self):
        """Main feature 1"""
        CF.good_morning()
        CF.show_days()
        CF.morning_briefing()
        CF.show_days()
        CF.copy_order_history()
        CF.game_round()
        CF.count_hours()
        assist_m.daily_report()

    def closing_venue(self):
        """update the budget and number of customers"""
        self.budgets_yesterday = self.budgets
        CF.closing_venue()
        CF.good_night()
        venue.days_addup()
        customers.add_customers()
        customers.lose_customers() # Sometimes customers leave with no reason
        venue.opening_venue()
venue = Venue()

class Customers:
    """main variable, customer number is changing every round"""
    def __init__(self):
        self.customers_number = 350
        self.happiness = 100
        self.happiness_yesterday = self.happiness

    def add_customers(self):
        """more customers on each days"""
        self.customers_number += 0.03 * self.customers_number * venue.difficulty + 5

    def lose_customers(self):
        """To control the number of customers if too many"""
        CF.lose_customers()

customers = Customers()

class Assist_M():
    """helper or guide of the game"""
    def __init__(self):
        self.bad_news = False
        self.percent_priceup = 0

    def greetings(self):
        """the rule is explained through here before the first round"""
        CF.rule_explain()
        venue.opening_venue()

    def daily_report(self):
        """Main feature 2
        report of every round then decide to adjust the prices of back order"""
        CF.show_days()
        CF.daily_report_scripts()
        CF.wastage_check()
        CS.main_story.check_passed()
        CF.bad_news()
        assist_m.place_orders()

    def place_orders(self):
        """Main feature 3"""
        CF.show_days()
        CF.place_order()
        venue.closing_venue()

    def tell_news(self):
        """roll the dice whether price up and how much"""
        self.percent_priceup = CF.percentage_priceup()
        if self.bad_news is True:
            venue.price_adj = 1 + self.percent_priceup
        elif self.bad_news is False:
            venue.price_adj = 1

assist_m = Assist_M()
