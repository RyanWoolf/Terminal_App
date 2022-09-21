from art import *
from time import sleep
import config_system as CS
import config_functions as CF


class Venue:
    def __init__(self):
        self.budgets = 10000
        self.budgets_yesterday = self.budgets
        self.days = 1
        self.list_foods = ["Beef burger", "Beef burger", "Beef burger", "Fish & chips", "Fish & chips", "Pizza", "Pizza"]
        self.list_drinks = ["Soft drink", "Soft drink", "Soft drink", "Coffee", "Coffee", "Beer"]
        self.current_stocks = {
            "Beef burger" : 150,
            "Fish & chips" : 100,
            "Pizza" : 100,
            "Soft drink" : 170,
            "Coffee" : 120,
            "Beer" : 60 }
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
        sleep(2)
        self.budgets_yesterday = self.budgets
        customers.happiness_yesterday = customers.happiness
        CF.show_days()
        sleep(1)
        if self.days == 1:
            CF.typing_animation("Luckily We have received urgent delivery from the supplier early morning.\n", 0.02)
        CF.typing_animation("\nToday, We got \n\n", 0.02)
        sleep(0.5)
        CF.print_current_stocks()
        sleep(1)
        CF.ready()
        CF.show_days()
        CF.round()
        CF.count_hours()
        assist_m.daily_report()
    
    def closing_venue(self):
        CF.closing_venue()
        CF.good_night()
        sleep(2)
        CF.enter_to_cont()
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
        tprint("Welcome\n\n", font= "tarty1")
        sleep(1)
        CF.typing_animation("Hi! My name is " + CS.color.BOLD + "Ryan" + CS.color.END+ " and I'm your assistant manager.\n", 0.02)
        sleep(0.5)
        CF.typing_animation("As you know, We have hired new staff recently. They're working fine but it would be better if we have a good captain to lead.\n", 0.02)
        sleep(0.5)
        CF.typing_animation("\nYour job is \n\n" + CS.color.YELLOW + "  to let me know what to order for the next day service and \n\n  give orders to staff when situation happens.\n" + CS.color.END, 0.02)
        sleep(0.5)
        CF.typing_animation("\nBut remember, You'll lose if you\n\n" + CS.color.RED + "  lose budget till $5000 or \n\n  lose Customers Satisfaction till 60% \n" + CS.color.END, 0.02)
        sleep(0.5)
        CF.typing_animation("\nI'm always here to assist you, give you tips and my opinions.\n", 0.02)
        sleep(0.5)
        CF.typing_animation("Good luck! :)\n\n", 0.02)
        sleep(1)
        CF.enter_to_cont()
        venue.opening_venue()
        
    def daily_report(self):
        CF.show_days()
        print("Daily Report : ")
        sleep(1)
        CF.daily_report_scripts()
        sleep(1)
        print("\nWe earned " + CS.color.YELLOW + f"$ {venue.budgets - venue.budgets_yesterday}" + CS.color.END + " today, Current balance is " + CS.color.YELLOW + f"$ {venue.budgets}" + CS.color.END)
        sleep(1)
        print("\nAnd, Todays our customers happiness is " + CS.color.YELLOW + f"{customers.happiness:.2f} % " + CS.color.END)
        sleep(2)
        CF.typing_animation("\n\nChecking the stocks left ...\n\n", 0.02)
        sleep(1)
        CF.print_current_stocks()
        sleep(1)
        CF.typing_animation("\nWe don't use the stock again. We'll dicard them and replace to fresh ones.\n", 0.02)
        sleep(1)
        CF.typing_animation("\nPlease let me know the stock orders for tomorrow service.\n", 0.02)
        sleep(1)
        CF.enter_to_cont()
        assist_m.place_orders()


    def place_orders(self):
        CF.show_days()
        print("Order list : \n\n")
        sleep(1)
        CF.order_list()


        
        
        pass
assist_m = Assist_M()

class Player:
    pass