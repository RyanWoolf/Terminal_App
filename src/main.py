from art import *
import config_system as CS
import config_functions as CF
import config_characters as CC

CF.clear_screen()
if __name__ == '__main__':
    try:
        CS.main_story.greetings()
        CS.main_story.select()

    except KeyboardInterrupt:
        CF.clear_screen()
        tprint("\n\nGood bye\n\n", font= "tarty1")
        print("Sorry to see you go. Hope to meet you soon again!\n\n")
