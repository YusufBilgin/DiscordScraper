import os
from pick import pick
from dotenv import load_dotenv
from colorama import Fore, init

from modules.menu import menu
from modules.utils import wait
from modules.cli_forms import choose_action
from modules.get_requests import Requests
from modules.operations import (
    user_guilds,
    user_friends,
    user_dm_channels,
    user_account_data,
    specific_channel_messages
)

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
                        user_account_data(req)
                    case 1:
                        user_friends(req)
                    case 2:
                        user_dm_channels(req)
                    case 3:
                        user_guilds(req)
                    case 4:
                        channel_id = input("channel id: ")
                        specific_channel_messages(channel_id, req)
                    case 5:
                        title = "select a channel"
                        options = list()
                        channels = list()
                        
                        for channel in req.get_dm_channels():
                            if not channel['recipients'][0]['username'].isascii():
                                continue
                            options.append(
                                f"{channel['recipients'][0]['username']}#{channel['recipients'][0]['discriminator']}"
                            )
                            channels.append(
                                f"{channel['id']}"
                            )

                        option, index = pick(options, title)
                        print_specific_channel_messages(channels[index], req)

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
        print(Fore.RED + str(error))
        print("the program has been stopped" + Fore.RESET)
