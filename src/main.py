import config_system as CS
import os
os.system('cls' if os.name == 'nt' else 'clear')
os.system('resize -s 208 70')
# os.system('mode, con: cols=208 lines=60')
if __name__ == '__main__':

    LW_Haus = CS.System()
    LW_Haus.start()

    print(f"{'Welcome':^200}")