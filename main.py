import requests as rq
import pandas as pd
import datetime
import time


def execute():
    url = 'https://visitjordan.gov.jo/travelcars/'
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    file = pd.read_csv(r'final.csv', header=0)
    for i in range(len(file.index)):
        data = {
            'gstdoc': file['الوجهة'][i],
            'txtName': file['الاسم'][i],
            'ddlNationality': file['الجنسية'][i],
            'txtPassportNu': file['رقم جواز السفر'][i],
            'txtIDNumber': file['الرقم الوطني'][i],
            'txtCarNumber': file['رقم السيارة'][i],
            'txtEmail': file['البريد الالكتروني'][i],
            'ddlCountryCode': file['رمز الدولة'][i],
            'txtMobile': file['رقم الاتصال'][i],
            'chAgreed3': 'true',
            'SubmitInvest': 'إرسال الطلب',
        }

        image_path = file['جواز السفر'][i] + '.jpg'
        with open(image_path, 'rb') as f:
            image_data = f.read()
        files = {'hdFileUpload2': ('image.jpg', image_data)}
        r = rq.post(url, headers=head, data=data, files=files)
        print(r)

def start():
    while True:
        now = datetime.datetime.now()
        if now.hour == 21 and 0 <= now.minute < 30:
            execute()
        time.sleep(1)




if __name__ == '__main__':
    start()




