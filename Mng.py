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
        self.headers = {
            "X-IBM-Client-Id": self.key,
            "X-IBM-Client-Secret": self.secret,
            "content-type": "application/json",
            "accept": "application/json",
        }

    def decode_response(self, response):
        if response.text:
            response_json = json.loads(response.text)
        else:
            response_json = {}

        if response.status_code == 200:
            response_desc = response_json
        else:
            response_desc = (
                response_json["error"] if response_json["error"] else response_json
            )

        return {"status": response.status_code, "result": response_desc}

    def make_request(self, method, endpoint, payload=None):
        self.get_token()

        url = f"{defs.MNG_URL}/{endpoint}"
        response = requests.request(method, url, json=payload, headers=self.headers)
        # return response.text
        return self.decode_response(response)

    def get_token(self):
        if self.token and self.token_expiry and datetime.now() < self.token_expiry:
            print("token süresi devam ediyor.")
            self.headers["Authorization"] = f"Bearer {self.token}"

        url = f"{defs.MNG_URL}/token"
        payload = {
            "customerNumber": self.username,
            "password": self.password,
            "identityType": 1,
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response_json = json.loads(response.text)

        if response.status_code == 200:
            self.token_expiry = datetime.strptime(
                response_json["refreshTokenExpireDate"], "%d.%m.%Y %H:%M:%S"
            )
            self.headers["Authorization"] = f"Bearer {response_json['jwt']}"
        else:
            return False

    def create_order(self, payload):
        return self.make_request("POST", "/standardcmdapi/createOrder", payload)

    def cancel_order(self, reference_id):
        return self.make_request("PUT", f"/standardcmdapi/cancelorder/{reference_id}")

    def create_barcode(self, payload):
        return self.make_request("POST", "/barcodecmdapi/createbarcode", payload)

    def get_order(self, reference_id):
        return self.make_request("GET", f"/standardqueryapi/getorder/{reference_id}")

    def get_shipment(self, reference_id):
        return self.make_request("GET", f"/standardqueryapi/getshipment/{reference_id}")

    def get_shipment_status(self, reference_id):
        return self.make_request(
            "GET", f"/standardqueryapi/getshipmentstatus/{reference_id}"
        )
