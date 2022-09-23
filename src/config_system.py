"""Bring all the functions using through all modules"""
import config_functions as CF
import config_characters as CC

class Color:
    """Quick access for text color in the app"""
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
    """ The entire game container"""
    def __init__(self):
        pass

    def greetings(self):
        """the screen when app is just excuted"""
        CF.show_logo()

    def select(self):
        """select the game mode"""
        print("\n1. Play\n\n2. Exit\n\n")
        selection = CF.input_check()
        if selection == 1:
            main_story.game_start()
        elif selection == 2:
            raise KeyboardInterrupt

    def game_start(self):
        """the game starts"""
        CF.clear_screen()
        CC.assist_m.greetings()

    def check_passed(self):
        """system will check whether player is passed or failed"""
        CF.checking_rules()

main_story = System()
