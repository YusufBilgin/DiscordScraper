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

        print(json_data)

        return None