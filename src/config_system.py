from art import * 
from time import sleep
import config_functions as CF
import config_characters as CC

class bold_color:           # Quick access for Text colors 
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
color = bold_color()


class System:
    title = text2art("LionWolf  Haus", font = "tarty8")
    sub_title = text2art("\n\nSelect one from the following", font = "strforek")

    def __init__(self):
        pass
    def start(self):
        print(f"{self.title}")
        print(f"{self.sub_title}")
        print("\n1. New Game \n\n2. Resume Game\n\n")
        selection = CF.input_check()
        if selection == 1:
            self.game_mode = New_Game()
        elif selection == 2:
            self.game_mode = Resume_Game()

class New_Game:
    def __init__(self):
        CF.clear_screen()
        CC.assist_m.greetings_00()
        


class Resume_Game:
    def __init__(self):
        pass
    