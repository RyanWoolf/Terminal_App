from random import gammavariate
from art import text2art # for use of typography
import config_functions as CF
import config_characters as CC

class Color:           # Quick access for Text colors
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
color = Color()


class System:
    title = text2art("LionWolf  Haus", font = "tarty1")
    sub_title = text2art("Restaurant Tycoon", font = "tarty2")
    game_menu = color.BOLD + "Select one from the following" + color.END

    def __init__(self):
        pass

    def greetings(self):
        print(f"{self.title}")
        print(f"\n{self.sub_title}\n\n")
        print(f"{self.game_menu}\n\n")

    def select(self):
        print("\n1. Game start\n\n2. Exit\n\n")
        selection = CF.input_check()
        if selection == 1:
            self.game_mode = NewGame()
        elif selection == 2:
            raise KeyboardInterrupt

    def check_passed(self):
        CF.checking_rules()

main_story = System()

class NewGame:
    def __init__(self):
        CF.clear_screen()
        CC.assist_m.greetings_00()
        