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
    title = text2art("LionWolf  Haus", font = "tarty8")
    sub_title = text2art("\n\nSelect one from the following", font = "strforek")

    def __init__(self):
        print(f"{self.title}")
        print(f"{self.sub_title}")

    def select(self):
        print("\n1. New Game \n\n2. Resume Game\n\n")
        selection = CF.input_check()
        if selection == 1:
            self.game_mode = NewGame()
        elif selection == 2:
            self.game_mode = ResumeGame()

class NewGame:
    def __init__(self):
        CF.clear_screen()
        CC.assist_m.greetings_00()
        


class ResumeGame:
    def __init__(self):
        pass

# class SaveGame: