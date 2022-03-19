import json
import requests


class Requests():
    def __init__(self, auth_token) -> None:
        self.headers = {
            'authorization': auth_token
        }

    def request_func(self, url):
        r = requests.get(
            url,
            headers = self.headers
        )
        return json.loads(r.text)

    def get_account_info(self) -> dict:
        return self.request_func(
            f'https://discord.com/api/v9/users/@me'
        )

    def get_friends(self) -> list:
        return self.request_func(
            f'https://discord.com/api/v9/users/@me/relationships'
        )

    def get_dm_channels(self) -> list:
        return self.request_func(
            f'https://discord.com/api/v9/users/@me/channels'
        )

    def get_guilds(self) -> list:
        return self.request_func(
            f'https://discord.com/api/v9/users/@me/guilds'
        )

    def get_channel_messages(self, channel_id, before = False, **kwargs):
        last_message_id = kwargs.get('id', None)

        if before == False:
            return self.request_func(
                f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50'
            )
        elif before == True:
            return self.request_func(
                f'https://discord.com/api/v9/channels/{channel_id}/messages?before={last_message_id}&limit=50'
            )
