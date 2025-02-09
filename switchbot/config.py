from dotenv import load_dotenv
load_dotenv()

import os

CLIENT_ID = os.getenv('CLIENT_TOKEN') 
CLIENT_SECRET = os.getenv('CLIENT_SECRET') 
POWER_BANK_1 = os.getenv('PLUGMINI_DEVICE_ID1') 