import os
from dotenv import load_dotenv
from modules.get_requests import Requests

load_dotenv()
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

req = Requests(AUTH_TOKEN)

req.get_account_info()