import definations as defs

from datetime import datetime
import json
import requests


class Mng:

    def __init__(self):
        self.token = None
        self.token_expiry = None
        self.username = defs.MNG_USER
        self.password = defs.MNG_PASS
        self.key = defs.MNG_KEY
        self.secret = defs.MNG_SECRET

    def get_token(self):
        if self.token and self.token_expiry and datetime.now() < self.token_expiry:
            print("token süresi devam ediyor.")
            return self.token

        url = f"{defs.MNG_URL}/mngapi/api/token"
        payload = {
            "customerNumber": self.username,
            "password": self.password,
            "identityType": 1,
        }
        headers = {
            "X-IBM-Client-Id": self.key,
            "X-IBM-Client-Secret": self.secret,
            "content-type": "application/json",
            "accept": "application/json",
        }
        response = requests.post(url, json=payload, headers=headers)
        response_json = json.loads(response.text)

        if response.status_code == 200:
            self.token_expiry = datetime.strptime(
                response_json["refreshTokenExpireDate"], "%d.%m.%Y %H:%M:%S"
            )
            return response_json["jwt"]
        else:
            return False

    def create_order(self, payload):
        self.token = self.get_token()

        if self.token:
            url = f"{defs.MNG_URL}/mngapi/api/standardcmdapi/createOrder"

            headers = {
                "X-IBM-Client-Id": self.key,
                "X-IBM-Client-Secret": self.secret,
                "Authorization": f"Bearer {self.token}",
                "content-type": "application/json",
                "accept": "application/json",
            }

            response = requests.post(url, json=payload, headers=headers)
            print(response.text)
            if response.status_code == 200:
                return {
                    "status": response.status_code,
                    "response": json.loads(response.text),
                }
            else:
                print(response.text)
                resp_json = json.loads(response.text)
                return (
                    resp_json["error"]["Description"]
                    if "Description" in resp_json["error"]
                    else resp_json["error"]["description"]
                )
