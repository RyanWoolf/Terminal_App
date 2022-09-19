import random as r
import time as t

beef_burger = 150
fish_chips = 100
pizza = 100

coffee = 100
soft_drink = 100
beer = 50
happyness = 100


while beef_burger > 0 and fish_chips > 0 and pizza > 0:
    start = t.time()
    menu_choice = r.randint(1, 100)
    drink_choice = r.randint(1, 100)
    if menu_choice > 57:
        beef_burger -= 1
    elif 30 < menu_choice <= 60: 
        fish_chips -= 1
    else:
        pizza -= 1
    t.sleep(0.01)
    end = t.time()
    print(end - start)


print(beef_burger, fish_chips, pizza)