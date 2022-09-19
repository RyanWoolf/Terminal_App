from art import * 
import config_functions as CF


class System:
    def __init__(self):
        tprint("LionWolf  Haus", "tarty8")
        tprint("\n\nSelect one from the following", "strforek")
        print("1. New Game \n2. Resume Game\n")
        CF.input_check(next)