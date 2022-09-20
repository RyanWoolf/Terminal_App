from art import *
import config_system as CS
import config_functions as CF
from time import sleep

class Venue:

    def __init__(self):
        self.budgets = 10000
        self.days = 1
        self.current_stocks = {
            "Beef burger" : 150,
            "Fish & chips" : 100,
            "Pizza" : 100,
            "Soft drink" : 170,
            "Coffee" : 120,
            "Beer" : 60 }
        
    def days_count(self):
        self.days += 1


class Customers:
    def __init__(self):
        self.happiness = 100

    pass


class Staffs:
    pass


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
        CF.typing_animation("Your job is \n\n" + CS.color.BOLD + "  to let me know what to order for the next day service and \n\n  give orders to staff when situation happens.\n" + CS.color.END, 0.02)
        sleep(0.5)
        CF.typing_animation("But remember, You'll lose if you\n\n" + CS.color.BOLD + "  lose half of budget or \n\n  lose Customers Satisfaction till 60% \n" + CS.color.END, 0.02)
        sleep(0.5)
        CF.typing_animation("I'm always here to assist you, give you tips and my opinions.\n", 0.02)
        sleep(0.5)
        CF.typing_animation("Good luck! :)\n", 0.02)
        CF.enter_to_cont()
        self.opening_venue()
        

    def opening_venue(self):
        CF.clear_screen()
        tprint(f"DAY {Venue.days}\n\n", font = "tarty3")
        if Venue.days == 1:
            CF.typing_animation("Luckily We have received urgent delivery from the supplier today.\n", 0.02)
            CF.typing_animation("We got \n", 0.02)
        for name, stock in Venue.current_stocks.items():
            print(f"{name} : {stock} ea\n")
        sleep(1)
        CF.typing_animation("\n\nI think we're ready to open.\n\n", 0.02)
        CF.enter_to_cont()


        

        
              



    def place_orders(self):
        
        pass


class Player:
    pass