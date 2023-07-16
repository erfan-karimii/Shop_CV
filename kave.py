# from kavenegar import *

# api = KavenegarAPI('61442F31622B6F695438514E3865524965345A395068304D6455444952526E6161653570554752357378673D')
# params = {'receptor': '09024485880', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
# response = api.sms_send(params)

import requests
id = 1

# for id in range(1,100):
id= 2
url = f'https://z.voorivex.academy/level-{id}/'
response = requests.get(url)
print(response.request)