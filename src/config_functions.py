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