import os
from dotenv import load_dotenv
from modules.get_requests import Requests

load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

req = Requests(AUTH_TOKEN)

print(req.get_account_info())
# friends = req.get_friends()

# print(friends)
