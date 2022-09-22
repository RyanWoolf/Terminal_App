from art import *
from time import sleep
import config_system as CS
import config_functions as CF


class Venue:
    def __init__(self):
        self.level = 1
        self.budgets = 10000
        self.budgets_yesterday = self.budgets
        self.days = 1
        self.list_foods = [
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

    def days_addup(self):
        self.days += 1

    def opening_venue(self):
        CF.good_morning()
        CF.show_days()
        CF.morning_briefing()
        CF.show_days()
        self.yesterday_stocks = self.current_stocks
        CF.game_round()
        CF.count_hours()
        assist_m.daily_report()

    def closing_venue(self):
        self.budgets_yesterday = self.budgets
        CF.closing_venue()
        CF.good_night()
        venue.days_addup()
        venue.opening_venue()
venue = Venue()

class Customers:
    def __init__(self):
        self.customers_number = 350  # Level can be applied
        self.happiness = 100
        self.happiness_yesterday = self.happiness

customers = Customers()

class Staffs:
    pass

staffs = Staffs()

class Assist_M(Staffs):
    def __init__(self):
        pass

    def greetings_00(self):
        CF.rule_explain()
        venue.opening_venue()

    def daily_report(self):
        CF.show_days()
        CF.daily_report_scripts()
        CF.wastage_check()
        assist_m.place_orders()

    def place_orders(self):
        CF.show_days()
        CF.place_order()

assist_m = Assist_M()

class Player:
    pass