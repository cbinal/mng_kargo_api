# MNG Kargo API Kullanım Klavuzu

## Yapılması gerekenler

- https://sandbox.mngkargo.com.tr/ adresinden bir kullanıcı oluşturulmalı
- Kullanıcı oluşturulduktan sonra panel üzerinden uygulama oluşturulmalı. (Daha sonra bu uygulamaya API ürünleri eklenecek)

## definations.py

```python
MNG_KEY = "xxxxxxxxxxxxxxxx"
MNG_SECRET = "xxxxxxxxxxxxxxxx"
MNG_USER = "xxxxxxxxxxxxxxxx"
MNG_PASS = "xxxxxxxxxxxxxxxx"
MNG_URL = "https://testapi.mngkargo.com.tr/mngapi/api"
```

## Sınıfın oluşturulması

```python
from Mng import Mng
mng = Mng()
```

## Standard Command API 1.0

createOrder, cancelOrder gibi metodların kullanılabilmesi için "Standard Command API 1.0" ürününün uygulamasınıza eklenmesi gerekmektedir.

### createOrder Alanları ve Açıklamaları

Normal gönderi oluşturulan metoddur.

Kullanımı :

```python
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

shipping = mng.create_order(payload)
```

#### order (Object)

Kargo genel bilgileri

| Alan Adı             | Zorunlu | Veri Tipi | Açıklama                                                                                             | Dğerler                                                  |
| -------------------- | ------- | --------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| referenceId          | X       | string    | Sipariş numarası her sipariş için benzersiz olmalıdır. Sipariş numarası büyükharflerden oluşmalıdır. |                                                          |
| barcode              |         | string    | Barkod ReferenceId ile aynı olmalıdır. Barkod büyükharflerden oluşmalıdır.                           |                                                          |
| billOfLandingId      |         | string    | Irsaliye Numarası                                                                                    |                                                          |
| isCOD                |         | integer   | Kapıda ödeme bilgisi                                                                                 | 1:Kapıda Ödeme                                           |
| codAmount            |         | float     | Kapıda ödeme tutarı                                                                                  |                                                          |
| shipmentServiceType  | X       | integer   | Gönderi Tipi                                                                                         | 1:STANDART_TESLİMAT, 7:GUNİCİ_TESLİMAT, 8:AKŞAM_TESLİMAT |
| packagingType        | X       | integer   | Kargo Cinsi                                                                                          | 1:DOSYA, 2:Mİ, 3:PAKET, 4:KOLİ                           |
| content              | X       | string    | içerik genel bilgisi                                                                                 |                                                          |
| smsPreference1       | X       | integer   | Branch Kargo varış şubesine ulaştığında alıcıya SMS gitsin mi?                                       | 1:Evet, 0:Hayır                                          |
| smsPreference2       | X       | integer   | Kargo ilk hazırlandığında alıcıya SMS gitsin mi?                                                     | 1: Evet, 0: Hayır                                        |
| smsPreference3       | X       | integer   | Kargo teslim edildiğinde göndericiye SMS gitsin mi?                                                  | 1: Evet, 0: Hayır                                        |
| paymentType          | X       | integer   | Ödeme Şekli, CreateOrder metodunda 3 tipindeki ödeme şekli geçerli değildir.                         | 1:GONDERICI_ODER, 2:ALICI_ODER, 3:PLATFORM_ODER          |
| deliveryType         | X       | integer   | Teslim Şekli                                                                                         | 1:ADRESE_TESLIM, 2:ALICISI_HABERLİ                       |
| description          | X       | string    | İçerik                                                                                               |                                                          |
| marketPlaceShortCode |         | string    | Pazaryeri Kodu                                                                                       | TRND, N11, GG, VIVE                                      |
| marketPlaceSaleCode  |         | string    | Pazaryeri Satış Kodu                                                                                 |                                                          |

#### orderPieceList (Array)

Kargo parçaları listesi

| Alan Adı | Zorunlu | Veri Tipi | Açıklama       |
| -------- | ------- | --------- | -------------- |
| barcode  | X       | string    | Barkod kodu    |
| desi     | X       | integer   | Parça Desi     |
| kg       | X       | integer   | Parça Ağırlığı |
| content  |         | string    | Paket içeriği  |

#### recipient (Object)

Kargo alıcısının bilgileri

| Alan Adı             | Veri Tipi | Açıklama                                             |
| -------------------- | --------- | ---------------------------------------------------- |
| customerId           | integer   | Müşteri numarası                                     |
| refCustomerId        | string    | Müşterinin kendi sistemindeki numarası               |
| cityCode             | integer   | Şehir Kodu, CBS Info API'den kod bilgisi alınabilir. |
| districtCode         | integer   | İlçe Kodu, CBS Info API'den kod bilgisi alınabilir.  |
| address              | string    | Adres                                                |
| bussinessPhoneNumber | string    | İş yeri telefon numarası                             |
| email                | string    | Mail adresi                                          |
| taxOffice            | string    | Vergi dairesi                                        |
| taxNumber            | string    | Vergi Numarası                                       |
| fullName             | string    | Müşterinin tam adı                                   |
| homePhoneNumber      | string    | Ev telefon numarası                                  |
| mobilePhoneNumber    | string    | Cep telefon numarası                                 |

#### createOrder Çıktısı

```python
{'status': 200, 'result': [{'orderInvoiceId': '1619005', 'orderInvoiceDetailId': '1619518', 'shipperBranchCode': '03401700', 'referenceId': 'SIPARIS22234567'}]}
```

### cancelOrder

createOrder ile oluşturulmuş gönderinin iptal edildiği metoddur.

## Barcode Command API 1.0

Oluşturulan kargo bu API ürünü ile faturalaştırılabilir. Kullanabilmek için ayrıca istekte bulunduğunuz IP nin MNG tarafında izne ihtiyacı vardır.
