import config_system as CS
import config_functions as CF
import config_characters as CC
from art import *

CF.clear_screen()
if __name__ == '__main__':
    try:
        main_story = CS.System()
        main_story.start()
    
    except KeyboardInterrupt:
        CF.clear_screen()
        tprint("Good bye\n\n", font= "tarty3")
        print("Sorry to see you go. Hope to meet you soon again!\n\n")

    