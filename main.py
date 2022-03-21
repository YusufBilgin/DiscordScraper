import os
from tabulate import tabulate
from dotenv import load_dotenv
from colorama import Fore, init

from modules.menu import menu
from modules.utils import wait
from modules.cli_forms import choose_action, save_or_not
from modules.file_operations import save_content_to_txt
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

        if user_input == 1 or user_input == "1":
            selected_action = choose_action()

            match selected_action:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case _:
                    pass

            if selected_action == 0:
                print_user_account_data(req)
                
            elif selected_action == 1:
                print_user_friends(req)

            elif selected_action == 2:
                print_user_dm_channels(req)

            elif selected_action == 3:
                print_user_guilds(req)

            elif selected_action == 4:
                channel_id = input("channel id: ")
                print_specific_channel_messages(channel_id, req)
            
            print("Press any key to continue")
            wait()

        elif user_input == 2 or user_input == "2":
            print("info text")
        else:
            print("Please choose a valid operation")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\nExit the program")
    except Exception as error:
        print(Fore.RED + error)
        print("the program has been stopped" + Fore.RESET)
