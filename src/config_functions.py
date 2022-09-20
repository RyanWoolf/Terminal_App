import config_system as CS
import os
from time import sleep
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('resize -s 208 70')
    # os.system('mode, con: cols=208 lines=70')

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
