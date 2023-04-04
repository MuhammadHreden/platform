import requests as rq
import pandas as pd
import datetime
import time


def execute():
    url = 'https://visitjordan.gov.jo/travelcars/'
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-GB,en;q=0.9,en-US;q=0.8',
        'cache-control': 'max-age=0',
        'content-length' : '2755',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryiHJNWyPfqTXtBhb1',
        'origin': 'null',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
    
    }
    file = pd.read_csv('final.csv', header=0)
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
        print(file['الاسم'][i])
        print(r)

def start():
    while True:
        now = datetime.datetime.now()
        if now.hour == 21 and 0 <= now.minute < 5:
            execute()
        time.sleep(1)




if __name__ == '__main__':
    start()




