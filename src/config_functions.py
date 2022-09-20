import config_system as CS
import config_characters as CC
import sys
import os
import random as r
from time import sleep


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    
def enter_to_cont():
    input("Please enter to continue")

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

def round():
    for customer in range(CC.customers.customers_number):
        menu_choice = r.randint(1, 100)
        if menu_choice > 55: # Level can be applied
            CC.venue.current_stocks["Beef burger"] -= 1
            if CC.venue.current_stocks["Beef burger"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Beef burger"] = 0
        elif 30 < menu_choice <= 55:
            CC.venue.current_stocks["Fish & chips"] -= 1
            if CC.venue.current_stocks["Fish & chips"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Fish & chips"] = 0
        else:
            CC.venue.current_stocks["Pizza"] -= 1
            if CC.venue.current_stocks["Pizza"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Pizza"] = 0
        sleep(0.005)
    for customer in range(CC.customers.customers_number):
        drink_choice = r.randint(1, 100)
        if drink_choice > 55: # Level can be applied
            CC.venue.current_stocks["Soft drink"] -= 1
            if CC.venue.current_stocks["Soft drink"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Soft drink"] = 0
        elif 20 < drink_choice <= 55:
            CC.venue.current_stocks["Coffee"] -= 1
            if CC.venue.current_stocks["Coffee"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Coffee"] = 0
        else:
            CC.venue.current_stocks["Beer"] -= 1
            if CC.venue.current_stocks["Beer"] < 0:
                CC.customers.happiness -= 0.5
                CC.venue.current_stocks["Beer"] = 0
    print(CC.customers.happiness)
       

