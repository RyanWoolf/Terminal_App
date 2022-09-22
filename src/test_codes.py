import random as r
import time as t

customers = 350 
happyness = 100.0 # keep it for the next round

# Stocks will be discarded after each round
beef_burger = 150 
fish_chips = 100
pizza = 100

soft_drink = 170
coffee = 120
beer = 60



start = t.time()
for customer in range(customers):
    menu_choice = r.randint(1, 100)
    if menu_choice > 55:
        beef_burger -= 1
        if beef_burger < 0:
            happyness -= 0.5
            beef_burger = 0
    elif 30 < menu_choice <= 55:
        fish_chips -= 1
        if fish_chips < 0:
            happyness -= 0.5
            fish_chips = 0
    else:
        pizza -= 1
        if pizza < 0:
            happyness -= 0.5
            pizza = 0
    t.sleep(0.005)
for customer in range(customers):
    drink_choice = r.randint(1, 100)
    if drink_choice > 55:
        soft_drink -= 1
        if soft_drink < 0:
            happyness -= 0.5
            soft_drink = 0
    elif 20 < drink_choice <= 55: 
        coffee -= 1
        if coffee < 0:
            happyness -= 0.5
            coffee = 0
    else:
        beer -= 1
        if beer < 0:
            happyness -= 0.5
            beer = 0
    t.sleep(0.005)
    
end = t.time()
print(end - start)

print(happyness)

print(beef_burger, fish_chips, pizza)
print(soft_drink, coffee, beer)