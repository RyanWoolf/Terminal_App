import random
import time as t

customers = 350 
 # keep it for the next round
difficulty = 1

list_foods = [ # More same names mean more preferences
            "Beef burger", "Beef burger", "Beef burger",
            "Fish & chips", "Fish & chips",
            "Pizza", "Pizza"]
list_drinks = [
            "Soft drink", "Soft drink", "Soft drink",
            "Coffee", "Coffee",
            "Beer"]
current_stocks = {
            "Beef burger" : 150,
            "Fish & chips" : 100,
            "Pizza" : 100,
            "Soft drink" : 170,
            "Coffee" : 120,
            "Beer" : 60 }
yesterday_stocks = {}
stock_prices = {
            "Beef burger" : 15,
            "Fish & chips" : 15,
            "Pizza" : 13,
            "Soft drink" : 4,
            "Coffee" : 5,
            "Beer" : 10 }
supplier_prices = {
            "Beef burger" : 7,
            "Fish & chips" : 6,
            "Pizza" : 5,
            "Soft drink" : 2,
            "Coffee" : 3,
            "Beer" : 5 }


def game_round(pax):
    customer = 0
    happiness = 100.0
    budgets = 0
    while customer < pax:
        food, drink = random.choice(list_foods), random.choice(list_drinks)
        current_stocks[food] -= 1
        current_stocks[drink] -= 1
        budgets += stock_prices[food] + stock_prices[drink]
        happiness += 0.2
        if current_stocks[food] < 0:
            happiness -= (0.6 * difficulty)
            current_stocks[food] = 0
            budgets -= stock_prices[food]
        if current_stocks[drink] < 0:
            happiness -= (0.6 * difficulty)
            current_stocks[drink] = 0
            budgets -= stock_prices[drink]
        customer += 1
    return budgets
print(game_round(100))
# Stocks will be discarded after each round
# beef_burger = 150 
# fish_chips = 100
# pizza = 100

# soft_drink = 170
# coffee = 120
# beer = 60

# for customer in range(customers):
#     menu_choice = r.randint(1, 100)
#     if menu_choice > 55:
#         beef_burger -= 1
#         if beef_burger < 0:
#             happyness -= 0.5
#             beef_burger = 0
#     elif 30 < menu_choice <= 55:
#         fish_chips -= 1
#         if fish_chips < 0:
#             happyness -= 0.5
#             fish_chips = 0
#     else:
#         pizza -= 1
#         if pizza < 0:
#             happyness -= 0.5
#             pizza = 0
#     t.sleep(0.005)
# for customer in range(customers):
#     drink_choice = r.randint(1, 100)
#     if drink_choice > 55:
#         soft_drink -= 1
#         if soft_drink < 0:
#             happyness -= 0.5
#             soft_drink = 0
#     elif 20 < drink_choice <= 55: 
#         coffee -= 1
#         if coffee < 0:
#             happyness -= 0.5
#             coffee = 0
#     else:
#         beer -= 1
#         if beer < 0:
#             happyness -= 0.5
#             beer = 0
#     t.sleep(0.005)

