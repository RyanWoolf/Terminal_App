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

def ready():
    typing_animation("\n\nWe're ready to open.\n\n", 0.02)
    enter_to_cont()

def round():
    for customer in range(CC.customers.customers_number):
        menu_choice = random.randint(1, 100)
        if menu_choice > 55: # Level can be applied
            CC.venue.current_stocks["Beef burger"] -= 1
            CC.venue.budgets += CC.venue.stock_prices["Beef burger"]
            if CC.venue.current_stocks["Beef burger"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Beef burger"] = 0
                CC.venue.budgets -= CC.venue.stock_prices["Beef burger"]
        elif 30 < menu_choice <= 55:
            CC.venue.current_stocks["Fish & chips"] -= 1
            CC.venue.budgets += CC.venue.stock_prices["Fish & chips"]
            if CC.venue.current_stocks["Fish & chips"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Fish & chips"] = 0
                CC.venue.budgets -= CC.venue.stock_prices["Fish & chips"]
        else:
            CC.venue.current_stocks["Pizza"] -= 1
            CC.venue.budgets += CC.venue.stock_prices["Pizza"]
            if CC.venue.current_stocks["Pizza"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Pizza"] = 0
                CC.venue.budgets -= CC.venue.stock_prices["Pizza"]
    for customer in range(CC.customers.customers_number):
        drink_choice = random.randint(1, 100)
        if drink_choice > 55: # Level can be applied
            CC.venue.current_stocks["Soft drink"] -= 1
            CC.venue.budgets += CC.venue.stock_prices["Soft drink"]
            if CC.venue.current_stocks["Soft drink"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Soft drink"] = 0
                CC.venue.budgets -= CC.venue.stock_prices["Soft drink"]
        elif 20 < drink_choice <= 55:
            CC.venue.current_stocks["Coffee"] -= 1
            CC.venue.budgets += CC.venue.stock_prices["Coffee"]
            if CC.venue.current_stocks["Coffee"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Coffee"] = 0
                CC.venue.budgets -= CC.venue.stock_prices["Coffee"]
        else:
            CC.venue.current_stocks["Beer"] -= 1
            CC.venue.budgets += CC.venue.stock_prices["Beer"]
            if CC.venue.current_stocks["Beer"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Beer"] = 0
                CC.venue.budgets -= CC.venue.stock_prices["Beer"]

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
