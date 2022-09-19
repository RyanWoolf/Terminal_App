from art import * 
import config_functions as CF


class System:
    title = text2art("LionWolf  Haus", font = "tarty8")
    sub_title = text2art("\n\nSelect one from the following", font = "strforek")

    def __init__(self):
        pass
    def start(self):
        print(f"{self.title}")
        print(f"{self.sub_title}")
        print("\n1. New Game \n\n2. Resume Game\n\n")
        CF.input_check(next)

class New_Game:
    def __init__(self):
        pass


class Resume_Game:
    def __init__(self):
        pass