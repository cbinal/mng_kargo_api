# MNG Kargo API Kullanım Klavuzu

## definations.py

```python
MNG_KEY = "xxxxxxxxxxxxxxxx"
MNG_SECRET = "xxxxxxxxxxxxxxxx"
MNG_USER = "xxxxxxxxxxxxxxxx"
MNG_PASS = "xxxxxxxxxxxxxxxx"
MNG_URL = "https://testapi.mngkargo.com.tr/mngapi/api"
```

## createOrder Alanları ve Açıklamaları

### order (Object)

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

### orderPieceList (Array)

Kargo parçaları listesi

| Alan Adı | Zorunlu | Veri Tipi | Açıklama       |
| -------- | ------- | --------- | -------------- |
| barcode  | X       | string    | Barkod kodu    |
| desi     | X       | integer   | Parça Desi     |
| kg       | X       | integer   | Parça Ağırlığı |
| content  |         | string    | Paket içeriği  |

### recipient (Object)

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

### createOrder Çıktısı

```python
[{"orderInvoiceId":"1618262","orderInvoiceDetailId":"1618775","shipperBranchCode":"03401700","referenceId":"SIPARIS134567"}]
{'status': 200, 'response': [{'orderInvoiceId': '1618262', 'orderInvoiceDetailId': '1618775', 'shipperBranchCode': '03401700', 'referenceId': 'SIPARIS134567'}]}
```
