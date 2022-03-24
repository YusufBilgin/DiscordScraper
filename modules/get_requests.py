import json
import requests


class Requests():
    def __init__(self, auth_token: str) -> None:
        self.headers = {
            'authorization': auth_token
        }

    def request_func(self, url: str):
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
    
    def get_guild_info(self, guild_id: str | int) -> list:
        return self.request_func(
            f'https://discord.com/api/v9/guilds/{guild_id}'
        )
    
    def get_guild_members(self, guild_id: str | int) -> dict:
        # (fix) endpoint is restricted
        return self.request_func(
            f'https://discord.com/api/v9/guilds/{guild_id}/members'
        )

    def get_guild_channels(self, guild_id: str | int) -> list:
        return self.request_func(
            f'https://discord.com/api/v9/guilds/{guild_id}/channels'
        )

    def get_channel_messages(self, channel_id: str | int, before: bool = False, **kwargs) -> list:
        last_message_id = kwargs.get('id', None)

        if before == False:
            return self.request_func(
                f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50'
            )
        elif before == True:
            return self.request_func(
                f'https://discord.com/api/v9/channels/{channel_id}/messages?before={last_message_id}&limit=50'
            )
