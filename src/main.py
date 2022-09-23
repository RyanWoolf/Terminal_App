"""main.py only works for initiating or ending a game"""
import config_system as CS
import config_functions as CF


CF.clear_screen()
if __name__ == '__main__':
    try:
        CS.main_story.greetings()
        CS.main_story.select()

    except KeyboardInterrupt:
        CF.clear_screen()
        CF.game_over()
