from tabulate import tabulate
from colorama import Fore, init
from .decorators import save_to_txt


@save_to_txt
def user_account_data(request_object: object) -> None:
        
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

    return data


def user_friends(request_object: object) -> None:
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


def user_dm_channels(request_object: object) -> None:
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


def user_guilds(request_object: object) -> None:
    guilds_raw = request_object.get_guilds()
    guilds = list()

    for i in guilds_raw:
        guilds.append({
            'Guild id': i['id'],
            'Name': Fore.MAGENTA + i['name'] + Fore.RESET,
        })

    print(tabulate(guilds, headers = 'keys', tablefmt = "github"))

    return None


def guild_channels(request_object: object, guild_id: str) -> dict:
    """makes a get request to get guild channels and simplifies response data

    Args:
        request_object (object): request object
        guild_id (str): Guild id as string 

    Returns:
        dict: contains all sound and text channels (id and name)
    """
    channels = {
        'text': [],
        'sound': []
    }

    row_data = request_object.get_guild_channels(guild_id)
    if type(row_data) == dict:
        # If this is dict its possibility an error message about missing auth
        print(Fore.RED + row_data['message'] + Fore.RESET)
        return None

    for i in row_data:
        try:
            if not i['last_message_id'] == None:
                channels['text'].append({
                    'id': i['id'],
                    'name': i['name'],
                })
            else:
                channels["sound"].append({
                    'id': i['id'],
                    'name': i['name']
                })
        except KeyError:
            continue

    return channels


def specific_channel_messages(channel_id: str, request_object: object) -> None:
    channel_messages_row = request_object.get_channel_messages(channel_id) 

    if type(channel_messages_row) == dict:
        print(Fore.RED + channel_messages_row['message'] + Fore.RESET)
        return None

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

    while True:
        for i in range(1):
            try:
                last_id = messages_list[-1]['Message id']
                row_data = request_object.get_channel_messages(channel_id, id = last_id, before = True)
                add_messages_to_list(messages_list, row_data)
            except:
                print(Fore.RED + "There is no more data to request" + Fore.RESET)
                break
        if len(row_data) < 50:
            print(Fore.GREEN + "There is no more data to request" + Fore.RESET)
            break
    
    for i in reversed(messages_list):
        print(f"{i['Message author']}: {i['content']}\n")

    return None