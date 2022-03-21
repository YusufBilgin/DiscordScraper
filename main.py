import os
from dotenv import load_dotenv
from colorama import Fore, init

from modules.menu import menu
from modules.utils import wait
from modules.cli_forms import choose_action
from modules.get_requests import Requests
from modules.operations import *

init()
load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

req = Requests(AUTH_TOKEN)


def main():
    menu()
    while True:  
        user_input = input("Please choose one of the actions given above: ")

        match user_input:
            case "1":
                selected_action = choose_action()
                match selected_action:
                    case 0:
                        print_user_account_data(req)
                    case 1:
                        print_user_friends(req)
                    case 2:
                        print_user_dm_channels(req)
                    case 3:
                        print_user_guilds(req)
                    case 4:
                        channel_id = input("channel id: ")
                        print_specific_channel_messages(channel_id, req)
                    case _:
                        pass

                print("Press any key to continue")
                wait()
            case "2":
                print("info text")
            case _:
                print("Please choose a valid operation")
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\nExit the program")
    except Exception as error:
        print(Fore.RED + error)
        print("the program has been stopped" + Fore.RESET)
