import os
from tabulate import tabulate
from dotenv import load_dotenv
from colorama import Fore, init

from modules.menu import menu
from modules.utils import wait
from modules.cli_forms import choose_action, save_or_not
from modules.file_operations import save_content_to_txt
from modules.get_requests import Requests

init()
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
                            'Channel id': i['id'],
                            'Username': Fore.CYAN + i['recipients'][0]['username'] + Fore.RESET,
                            'Discord id': f"{i['recipients'][0]['username']}#{i['recipients'][0]['discriminator']}",
                            'User avatar': f'\u001b]8;;{avatar_link}\u001b\\View Avatar\u001b]8;;\u001b\\'
                        })
                
                print(tabulate(dm_channels, headers = 'keys', tablefmt = "grid"))

            elif selected_action == 3:
                guilds_raw = req.get_guilds()
                guilds = list()

                for i in guilds_raw:
                    guilds.append({
                        'Guild id': i['id'],
                        'Name': Fore.MAGENTA + i['name'] + Fore.RESET,
                    })

                print(tabulate(guilds, headers = 'keys', tablefmt = "github"))

            elif selected_action == 4:
                channel_id = input("channel id: ")
                channel_messages_row = req.get_channel_messages(channel_id) 
                messages_list = list()

                def add_messages_to_list(message_list, row_data) -> list:
                    for i in row_data:
                        message_list.append({
                            'Message id': i['id'],
                            'Message author': i['author']['username'],
                            'content': i['content'],
                            'time': i['timestamp']
                        })

                    return message_list

                messages_list = add_messages_to_list(messages_list, channel_messages_row)

                n = 25  # The for loop should run until there is no message. idk how to do this
                for i in range(0, n):
                    try:
                        last_id = messages_list[-1]['Message id']
                        add_messages_to_list(messages_list, req.get_channel_messages(channel_id, id = last_id, before = True))
                    except:
                        print(Fore.RED + "There is no more data to request" + Fore.RESET)
                        break
                

                for i in reversed(messages_list):
                    print(f"{i['Message author']}: {i['content']}\n")


            
            print("Press any key to continue")
            wait()

        elif user_input == 2:
            print("info text")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\nExit the program")
    except Exception as error:
        print(Fore.RED + error)
        print("the program has been stopped" + Fore.RESET)
