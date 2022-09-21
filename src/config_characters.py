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
        
    def days_addup(self):
        self.days += 1
    
    def opening_venue(self):
        CF.show_days()
        self.budgets_yesterday = self.budgets
        sleep(1)
        if self.days == 1:
            CF.typing_animation("Luckily We have received urgent delivery from the supplier early morning.\n", 0.02)
        CF.typing_animation("Today, We got \n", 0.02)
        sleep(0.5)
        for name, stock in self.current_stocks.items():
            print(f"{name} : {stock} ea\n")
            sleep(0.2)
        sleep(1)
        CF.ready()
        CF.show_days()
        CF.round()
        CF.count_hours()
        assist_m.daily_report()
venue = Venue()

class Customers:
    def __init__(self):
        self.customers_number = 350  # Level can be applied
        self.happiness = 100
    
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
        CF.typing_animation("\nYour job is \n\n" + CS.color.BOLD + "  to let me know what to order for the next day service and \n\n  give orders to staff when situation happens.\n" + CS.color.END, 0.02)
        sleep(0.5)
        CF.typing_animation("\nBut remember, You'll lose if you\n\n" + CS.color.BOLD + "  lose budget till $5000 or \n\n  lose Customers Satisfaction till 60% \n" + CS.color.END, 0.02)
        sleep(0.5)
        CF.typing_animation("\nI'm always here to assist you, give you tips and my opinions.\n", 0.02)
        sleep(0.5)
        CF.typing_animation("Good luck! :)\n\n", 0.02)
        sleep(1)
        CF.enter_to_cont()
        venue.opening_venue()
        
    def daily_report(self):
        CF.clear_screen()
        tprint(f"DAY {venue.days}\n\n", font = "tarty3")
        print("Daily Report : ")
        sleep(1)
        CF.daily_report_scripts()
        sleep(1)
        print(f"We earned $ {venue.budgets - venue.budgets_yesterday} today,")
        sleep(0.5)
        print(f"Current Balance is $ {venue.budgets}")
        sleep(1)
        print(f"And, current our customers happiness is {customers.happiness:.2f} % ")
        sleep(1)
        CF.typing_animation("")

    def place_orders(self):
        
        pass
assist_m = Assist_M()

class Player:
    pass