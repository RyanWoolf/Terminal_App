from art import *
import config_system as CS
import config_functions as CF
from time import sleep


class Venue:
    budgets = 0
    def __init__(self):
        self.budgets += 10000
        
    pass



class Customers:
    pass



class Staffs:
    pass


class Assist_M(Staffs):
    def __init__(self):
        pass
        
        

    def greetings(self):
        tprint("Welcome\n\n", font= "tarty1")
        sleep(1)
        CF.typing_animation("Hi! My name is " + CS.color.BOLD + "Ryan" + CS.color.END+ " and I'm your assistant manager.", 0.02)


class Player:
    pass