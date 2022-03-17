import os
import msvcrt as m
from pick import pick
from dotenv import load_dotenv
from colorama import Fore, Back, Style
from modules.get_requests import Requests
from tabulate import tabulate


load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

req = Requests(AUTH_TOKEN)


def wait():
    m.getch()

def choose_action():
    title = 'Please choose an action'
    options = [
        'Print my account infos',
        'Print my friends list',
        'Print my dm channels',
        'Print messages from a spesific channel'
    ]
    option, index = pick(options, title)

    return index
    
def calc_space(string_length, before_length, max_length):
    a = int(max_length) - (int(before_length) + int(string_length))
    space = a * " "

    return str(space)


print("""
    #########################################
    #                                       #
    #      Welcome to Discord Scraper       #
    #                                       #
    # {}{}
    #  {}  {}                  #
    #  {}  {}                            #
    #                                       #
    #########################################
    """.format(
            Fore.CYAN + 'Options:' + Style.RESET_ALL,
            calc_space(len('Options:'), 1, 39) + '#',
            Fore.CYAN + '[1]' + Style.RESET_ALL,
            'Choose actions',
            Fore.CYAN + '[2]' + Style.RESET_ALL,
            'Info'
        )
    )

try:
    while True:  
        user_input = int(
                input("Please choose one of the actions given above: ")
            )

        if user_input == 1:
            selected_action = choose_action()

            if selected_action == 0:
                user_account_data = req.get_account_info()
                table = [
                    ['ID', user_account_data['id']],
                    ['Username', user_account_data['username']],
                    ['Discriminator', user_account_data['discriminator']],
                    ['Location', user_account_data['locale']],
                    ['Email', user_account_data['email']],
                    ['Phone', user_account_data['phone']]
                ]
                print(
                    tabulate(table, headers = ['Name', 'Value'])
                )
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
                pass
            elif selected_action == 3:
                pass
            




            print("Press any key to continue")
            wait()
        elif user_input == 2:
            print("info text")
except KeyboardInterrupt:
    print("\nExit the program")
except Exception:
    print("the program has been stopped")
