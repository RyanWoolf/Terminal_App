import config_system as CS
import config_characters as CC
import sys, os, random
from art import *
from time import sleep


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    
def enter_to_cont():
    input("Please enter to continue ")

def typing_animation(text, speed):
    for letter in text:
        sleep(speed) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("")

def input_check():
    select_right = False
    while select_right == False:
        select = input("Select : ")
        if select == "1":
            select_right = True
            return int(select)
        elif select == "2":
            select_right = True
            return int(select)
        else:
            print(CS.color.RED + "Please enter the right number\n" + CS.color.END)

def show_days():
    clear_screen()
    tprint(f"DAY {CC.venue.days}\n\n", font = "tarty3")
    print(f"Current Balance : $ {CC.venue.budgets_yesterday}  |  Customers Happiness : {CC.customers.happiness_yesterday:.2f} %\n\n")

def good_morning():
    clear_screen()
    tprint("Good Morning", font = "tarty9")

def good_night():
    clear_screen()
    tprint("Good Night\n\n", font = "tarty9")

def ready():
    typing_animation("\n\nWe're ready to open.\n\n", 0.02)
    enter_to_cont()
    

def round():
    for customer in range(CC.customers.customers_number):
        food_choice, drink_choice = random.choice(CC.venue.list_foods), random.choice(CC.venue.list_drinks)
        CC.venue.current_stocks[food_choice] -= 1
        CC.venue.current_stocks[drink_choice] -= 1
        CC.venue.budgets += CC.venue.stock_prices[food_choice] + CC.venue.stock_prices[drink_choice]
        CC.customers.happiness += 0.2
        if CC.venue.current_stocks[food_choice] < 0:
            CC.customers.happiness -= 0.6
            CC.venue.current_stocks[food_choice] = 0
            CC.venue.budgets -= CC.venue.stock_prices[food_choice]
        if CC.venue.current_stocks[drink_choice] < 0:
            CC.customers.happiness -= 0.6
            CC.venue.current_stocks[drink_choice] = 0
            CC.venue.budgets -= CC.venue.stock_prices[drink_choice]
        if CC.customers.happiness > 100:
            CC.customers.happiness = 100
      
def count_hours():
    for time in range(9, 16):
        if time < 12:
            print(f"\n{time} AM ...")
        elif time == 12:
            print(f"\n{time} PM ...")
        else:
            print(f"\n{time - 12} PM ...")
        sleep(1)
    sleep(2)
    typing_animation("\n\nWe're closed now!", 0.02)
    sleep(1)
    typing_animation("\n\nI'll go get the daily report.\n\n", 0.02)
    sleep(1)
    enter_to_cont()

def daily_report_scripts():
    if CC.customers.happiness > 90:
        typing_animation("\n\nIt was great day!\n", 0.02)
        sleep(0.5) 
        typing_animation("I think our customers were super happy today!\n", 0.02) 
    elif 80 < CC.customers.happiness < 91:
        typing_animation("\n\nIt was good day!\n", 0.02)
        sleep(0.5) 
        typing_animation("We did good job generally.\n", 0.02)
    else:
        typing_animation("\n\nIt wasn't bad day.\n", 0.02)
        sleep(0.5) 
        typing_animation("But it seems like we need to do something to make it better.\n", 0.02)

def print_current_stocks():
    for name, stock in CC.venue.current_stocks.items():
        print(f"    {name} : {stock} ea\n")
        sleep(0.2)

def closing_venue():
    show_days()
    typing_animation("\n\nThe orders have been placed. THey'll be deliverd over the night.", 0.02)
    sleep(1)
    typing_animation("\n\nI'll see you tomorrow. :) \n\n", 0.02)
    sleep(1)
    enter_to_cont()



def order_list():
    payments_due = 0
    for name in CC.venue.current_stocks.keys():
        while True:
            units = input(name + " is $ " + f"{CC.venue.supplier_prices[name]}" + " : How many units to order?  ")
            try:
                CC.venue.current_stocks.update({name : int(units)})
                payments_due += int(units) * CC.venue.supplier_prices[name]
            except ValueError:
                print(CS.color.RED + "Please enter the right number\n" + CS.color.END)
                continue
            finally:
                print("")
            break
    sleep(0.5)
    print("\n\nThe below is order for tomorrow.\n\n")
    print_current_stocks()
    print(f"\n\nThe total payments due is $ {payments_due}\n\n")
    print("Is it correct?\n\n   1) Yes\n   2) No\n")
    selection = input_check()
    if selection == 1:
        print(f"\n\nYou have paid $ {payments_due} for the orders and $ {CC.venue.daily_staffs_wage} for daily wages.\n\n")
        CC.venue.budgets -= (payments_due + CC.venue.daily_staffs_wage)
        sleep(2)
        enter_to_cont()        
        CC.venue.closing_venue()
    elif selection == 2:
        CC.assist_m.place_orders()




            

            