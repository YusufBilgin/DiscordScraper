from tabulate import tabulate
from colorama import Fore, init
from .cli_forms import save_or_not
from .file_operations import save_content_to_txt

def print_user_account_data(request_object) -> None:
    if save_or_not() == 0:
        save = True
    else:
        save = False
        
    user_account_data = request_object.get_account_info()
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

    return None

def print_user_friends(request_object) -> None:
    user_friends = request_object.get_friends()
                
    for i in user_friends:
        table = [
            ['ID', i['user']['id']],
            ['Username', i['user']['username']],
            ['Discriminator', i['user']['discriminator']],
        ]
        print(
            tabulate(table)
        )

    return None

def print_user_dm_channels(request_object) -> None:
    dm_channels_row = request_object.get_dm_channels()
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

    return None

def print_user_guilds(request_object) -> None:
    guilds_raw = request_object.get_guilds()
    guilds = list()

    for i in guilds_raw:
        guilds.append({
            'Guild id': i['id'],
            'Name': Fore.MAGENTA + i['name'] + Fore.RESET,
        })

    print(tabulate(guilds, headers = 'keys', tablefmt = "github"))

    return None

def print_specific_channel_messages(channel_id, request_object) -> None:
    channel_messages_row = request_object.get_channel_messages(channel_id) 
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
            add_messages_to_list(messages_list, request_object.get_channel_messages(channel_id, id = last_id, before = True))
        except:
            print(Fore.RED + "There is no more data to request" + Fore.RESET)
            break
    

    for i in reversed(messages_list):
        print(f"{i['Message author']}: {i['content']}\n")

    return None