import json
import requests


class Requests():
    def __init__(self, auth_token) -> None:
        self.headers = {
            'authorization': auth_token
        }
        

    def get_account_info(self):
        r = requests.get(
            f'https://discord.com/api/v9/users/@me',
            headers = self.headers
        )
        json_data = json.loads(r.text)

        return json_data


    def get_friends(self):
        r = requests.get(
            f'https://discord.com/api/v9/users/@me/relationships',
            headers = self.headers
        )
        json_data = json.loads(r.text)
        
        return json_data

    def get_dm_channels(self):
        r = requests.get(
            f'https://discord.com/api/v9/users/@me/channels',
            headers = self.headers
        )
        json_data = json.loads(r.text)

        return json_data

    
    def get_dm_messages(self, channel_id, before = False, **kwargs):
        last_message_id = kwargs.get('id', None)

        if before == False:
            r = requests.get(
                f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', 
                headers = self.headers
            )
        elif before == True:
            r = requests.get(
                f'https://discord.com/api/v9/channels/{channel_id}/messages?before={last_message_id}&limit=50',
                headers = self.headers
            )
        json_data = json.loads(r.text)

        return json_data
