from email import header
import os
import msvcrt as m
from pick import pick
from tabulate import tabulate
from dotenv import load_dotenv

from modules.menu import *
from modules.utils import *
from modules.cli_forms import *
from modules.file_operations import *
from modules.get_requests import Requests


load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

req = Requests(AUTH_TOKEN)


def main():
    menu()
    while True:  
        user_input = int(
                input("Please choose one of the actions given above: ")
            )

        if user_input == 1:
            selected_action = choose_action()

            if selected_action == 0:
                if save_or_not() == 0:
                    save = True
                else:
                    save = False
                    
                user_account_data = req.get_account_info()
                table = [
                    ['ID', user_account_data['id']],
                    ['Username', user_account_data['username']],
                    ['Discriminator', user_account_data['discriminator']],
                    ['Location', user_account_data['locale']],
                    ['Email', user_account_data['email']],
                    ['Phone', user_account_data['phone']]
                ]
                data = tabulate(table, headers = ['Name', 'Value'])
                print(data)
                
                if save == True:
                    save_content_to_txt(data)
                
            elif selected_action == 1:
                user_friends = req.get_friends()
                
                for i in user_friends:
                    table = [
                        ['ID', i['user']['id']],
                        ['Username', i['user']['username']],
                        ['Discriminator', i['user']['discriminator']],
                    ]
                    print(
                        tabulate(table)
                    )

            elif selected_action == 2:
                dm_channels_row = req.get_dm_channels()
                dm_channels = list()

                for i in dm_channels_row:
                    avatar_link = "https://cdn.discordapp.com/avatars/{}/{}".format(
                        i['recipients'][0]['id'],
                        i['recipients'][0]['avatar']
                    )
                    dm_channels.append({
                            'channel_id': i['id'],
                            'username': i['recipients'][0]['username'],
                            'discord id': f"{i['recipients'][0]['username']}#{i['recipients'][0]['discriminator']}",
                            'User avatar': f'\u001b]8;;{avatar_link}\u001b\\View Avatar\u001b]8;;\u001b\\'
                        })
                
                print(tabulate(dm_channels, headers = 'keys', tablefmt="grid"))

            elif selected_action == 3:
                pass
            
            print("Press any key to continue")
            wait()

        elif user_input == 2:
            print("info text")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExit the program")
    except Exception as error:
        print(error)
        print("the program has been stopped")
