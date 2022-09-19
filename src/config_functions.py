import config_system as CS

def input_check(otherfunction):
    select_right = False
    while select_right == False:
        select = input("Select : ")
        if select == "1":
            select_right = True
            otherfunction
        elif select == "2":
            select_right = True
            otherfunction
        else:
            print("\033[31m" + "Please enter the right number\n" + "\033[0m")
