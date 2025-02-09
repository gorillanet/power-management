import os
import time
import json
import hashlib
import hmac
import base64
import uuid
import requests
import json
import datetime
from os.path import exists
import config


def request_to_swbot(endpoint):
    token = config.CLIENT_ID
    secret = config.CLIENT_SECRET
    nonce = str(uuid.uuid4())
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )

    apiHeader = {}
    apiHeader["Authorization"] = token
    apiHeader["Content-Type"] = "application/json"
    apiHeader["charset"] = "utf8"
    apiHeader["t"] = str(t)
    apiHeader["sign"] = str(sign, "utf-8")
    apiHeader["nonce"] = nonce

    response = requests.get(endpoint, headers=apiHeader)
    return response.json()


devices = request_to_swbot("https://api.switch-bot.com/v1.1/devices")

print(devices)