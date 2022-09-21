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
    tprint(f"\n   DAY {CC.venue.days}\n\n", font = "tarty3")
    balance = CC.venue.budgets_yesterday
    happiness = CC.customers.happiness_yesterday
    if balance >= 10000:
        colour_warning1 = CS.color.GREEN
    elif 7000 <= balance < 10000:
        colour_warning1 = CS.color.YELLOW
    elif balance < 7000:
        colour_warning1 = CS.color.RED 
    if happiness >= 85:
        colour_warning2 = CS.color.GREEN
    elif 70 <= happiness < 85:
        colour_warning2 = CS.color.YELLOW
    elif happiness < 70:
        colour_warning2 = CS.color.RED
    print(f"Current Balance : $ " + colour_warning1 + f"{balance:.2f}" + CS.color.END + "  |  Customers Happiness : " + colour_warning2 + f"{happiness:.2f}" + CS.color.END + " %")
    print("----------------------------------------------------------------\n\n")
    sleep(1)



def rule_explain():
    tprint("Welcome\n\n", font= "tarty1")
    sleep(1)
    typing_animation("Hi! My name is " + CS.color.BOLD + "Ryan" + CS.color.END+ " and I'm your assistant manager.\n", 0.02)
    sleep(0.5)
    typing_animation("As you know, We have hired new staff recently. They're working fine but it would be better if we have a good captain to lead.\n", 0.02)
    sleep(0.5)
    typing_animation("\nYour job is \n\n" + CS.color.YELLOW + "  to let me know what to order for the next day service and \n\n  give orders to staff when situation happens.\n" + CS.color.END, 0.02)
    sleep(0.5)
    typing_animation("\nBut remember, You'll lose if you\n\n" + CS.color.RED + "  lose budget till $5000 or \n\n  lose Customers Satisfaction till 60% \n" + CS.color.END, 0.02)
    sleep(0.5)
    typing_animation("\nI'm always here to assist you, give you tips and my opinions.\n", 0.02)
    sleep(0.5)
    typing_animation("\nand remember, Whenever you hit " + CS.color.BLUE + "Ctrl + C" + CS.color.END + ", You can exit the game.\n", 0.02)
    sleep(0.5)
    typing_animation("Good luck! :)\n\n", 0.02)
    sleep(1)
    enter_to_cont()


def good_morning():
    show_days()
    tprint("Good Morning", font = "tarty9")
    sleep(2)



def morning_briefing():
    if CC.venue.days == 1:
        typing_animation("Luckily We have received urgent delivery from the supplier early morning.\n", 0.02)
    typing_animation("\nToday, We got \n\n", 0.02)
    sleep(0.5)
    print_current_stocks()
    sleep(1)
    typing_animation("\n\nWe're ready to open.\n\n", 0.02)
    enter_to_cont()



def good_night():
    show_days()
    tprint("Good Night\n\n", font = "tarty9")
    sleep(1)
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
            print(f"\n  {time} AM ...")
        elif time == 12:
            print(f"\n  {time} PM ...")
        else:
            print(f"\n  {time - 12} PM ...")
        sleep(1)
    sleep(2)
    typing_animation("\n\nWe're closed now!", 0.02)
    sleep(1)
    typing_animation("\n\nI'll go get the daily report.\n\n", 0.02)
    sleep(1)
    enter_to_cont()



def daily_report_scripts():
    print("Daily Report : ")
    sleep(1)
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
    sleep(1)
    print("\nWe earned $ " + CS.color.YELLOW + f"{CC.venue.budgets - CC.venue.budgets_yesterday}" + CS.color.END + " today, Current balance is $ " + CS.color.YELLOW + f"{CC.venue.budgets}" + CS.color.END)
    CC.venue.budgets_yesterday = CC.venue.budgets
    sleep(1)
    print("\nAnd, Todays our customers happiness is " + CS.color.YELLOW + f"{CC.customers.happiness:.2f} " + CS.color.END + "%")
    CC.customers.happiness_yesterday = CC.customers.happiness
    sleep(2)



def wastage_check():
    typing_animation("\n\nChecking the stocks left ...\n\n", 0.02)
    sleep(1)
    print_current_stocks()
    sleep(1)
    num_wastage = 0
    price_wastage = 0
    for menu, stock in CC.venue.current_stocks.items():
        num_wastage += stock
        price_wastage += CC.venue.stock_prices[menu] * stock
    if num_wastage > 50:
        typing_animation(f"\nWe have {num_wastage} ea wastage today. That was $ " + CS.color.BLUE + f"{price_wastage:.2f}" + CS.color.END + " worths. \n\nI think we need to be careful on next stocks.", 0.02)
    elif num_wastage < 50:
        typing_animation(f"\nWe have $ " + CS.color.BLUE + f"{price_wastage:.2f}" + CS.color.END + " worths of loss today.", 0.02)
    typing_animation("\nWe don't use the stock again. We'll dicard them and replace to fresh ones.\n", 0.02)
    sleep(1)
    typing_animation("\nPlease let me know the stock orders for tomorrow service.\n", 0.02)
    sleep(1)
    enter_to_cont()



def print_current_stocks():
    for name, stock in CC.venue.current_stocks.items():
        print(f"    {name} : {stock} ea\n")
        sleep(0.2)



def closing_venue():
    show_days()
    typing_animation("\n\nThe orders have been placed. They'll be deliverd over the night.", 0.02)
    sleep(1)
    typing_animation("\n\nI'll see you tomorrow. :) \n\n", 0.02)
    sleep(1)
    enter_to_cont()



def place_order():
    payments_due = 0
    print("Order list : \n\n")
    sleep(1)
    for name in CC.venue.current_stocks.keys():
        while True:
            units = input(name + " is $ " + CS.color.BLUE + f"{CC.venue.supplier_prices[name]:.2f}" + CS.color.END + f". How many units to order? Yeseterday : {CC.venue.yesterday_stocks[name]} ea / Today : ")
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
    print(f"\n\nThe total payments due is $ " + CS.color.YELLOW + f"{payments_due:.2f}" + CS.color.END + "and the daily wage for staffs is $ " + CS.color.YELLOW + f"{CC.venue.daily_staffs_wage:.2f}\n\n" + CS.color.END)
    if payments_due + CC.venue.daily_staffs_wage > CC.venue.budgets:
        print(CS.color.RED + "It's over your current balance. Please change the amount of order.\n\n" + CS.color.END)
        sleep(1)
        enter_to_cont()
        CC.assist_m.place_orders()
    print("Is it correct?\n\n   1) Yes\n   2) No\n")
    selection = input_check()
    if selection == 1:
        print(f"\n\nYou have paid $ " + CS.color.BLUE + f"{payments_due + CC.venue.daily_staffs_wage:.2f}" + CS.color.END + " altogether.\n\n")
        CC.venue.budgets -= (payments_due + CC.venue.daily_staffs_wage)
        sleep(2)
        enter_to_cont()        
        CC.venue.closing_venue()
    elif selection == 2:
        CC.assist_m.place_orders()




            

            