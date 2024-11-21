from Mng import Mng

mng = Mng()

payload = {
    "order": {
        "referenceId": "SIPARIS22234567",
        "barcode": "SIPARIS22234567",
        "billOfLandingId": "İrsaliye 1",
        "isCOD": 0,
        "codAmount": 0,
        "shipmentServiceType": 1,
        "packagingType": 1,
        "content": "İçerik 1",
        "smsPreference1": 1,
        "smsPreference2": 0,
        "smsPreference3": 0,
        "paymentType": 1,
        "deliveryType": 1,
        "description": "Açıklama 1",
        "marketPlaceShortCode": "",
        "marketPlaceSaleCode": "",
        "pudoId": "",
    },
    "orderPieceList": [
        {
            "barcode": "SIPARIS34567_PARCA1",
            "desi": 2,
            "kg": 1,
            "content": "Parça açıklama 1",
        },
        {
            "barcode": "SIPARIS34567_PARCA2",
            "desi": 2,
            "kg": 3,
            "content": "Parça açıklama 2",
        },
    ],
    "recipient": {
        "customerId": 58513278,
        "refCustomerId": "",
        "cityCode": 0,
        "cityName": "",
        "districtName": "",
        "districtCode": 0,
        "address": "",
        "bussinessPhoneNumber": "",
        "email": "",
        "taxOffice": "",
        "taxNumber": "",
        "fullName": "",
        "homePhoneNumber": "",
        "mobilePhoneNumber": "",
    },
}
# shipping = mng.create_order(payload)
# print(shipping)

query = mng.get_order(reference_id="SIPARIS12234567")
print(query)

# query = mng.get_shipment(reference_id="SIPARIS12234567")
# print(query)
#
# query = mng.get_shipment_status(reference_id="SIPARIS12234567")
# print(query)
