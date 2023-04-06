import requests as rq
import pandas as pd
import datetime
import time


str_arr = []

def execute():
    url = 'https://visitjordan.gov.jo/travelcars/'

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    for i in range(str_arr.shape[0]):
        data = {
            'gstdoc': str_arr[i][1],
            'txtName': str_arr[i][0],
            'ddlNationality': str_arr[i][2],
            'txtPassportNu': str_arr[i][3],
            'txtIDNumber': str_arr[i][4],
            'txtCarNumber': str_arr[i][5],
            'txtEmail': str_arr[i][6],
            'ddlCountryCode': "00"+str_arr[i][7],
            'txtMobile': "0"+str_arr[i][8],
            'chAgreed3': 'true',
            'SubmitInvest': 'إرسال الطلب',
        }

        image_path = str_arr[i][9] + '.jpg'
        files = {'hdFileUpload2': open(image_path, 'rb')}
        r = rq.post(url, headers=head, data=data, files=files)
        print(r)


def start():
    while True:
        now = datetime.datetime.now()
        if now.hour == 13 and 24 <= now.minute < 25:
            execute()


if __name__ == '__main__':
    file = pd.read_csv(r'final.csv', header=0)
    arr = file.to_numpy()
    str_arr = arr.astype(str)
    start()







'''
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
            '__EVENTTARGET': '',
            '__EVENTARGUMENT':'',
            '__EVENTVALIDATION': '/wEdABO8qXXx/PM5nvkxWx2nv9eh8pvA6+HFiCl2huAXpz01Y9KB7S1C83NSNsQV6CvLMBCjOglmm5fGSk5UkpFsfK4e7VtKE9rGcKIq9zB9tn8FNOtUGMXIm4ud9rQzDakoQ189UyUkYpYljjxmvP51O4Ji5ypIwEMtGPIuWgpB9qJ/iltFH9tc+7BVIcJl0mPxnsTFUq8ZnQpxppV6Fzb25WmYQwdmH1m48FGJ7a8D8d+hEqHKW+l4YRR74wP3PeXQDk82N/qoGeWkR8EN6Ipy558cjD1Ar0er+dzDqJIZ4xx6rxXE3dkwa1cRACVa3MHp4BtnAbvqdf0k8lvizRTuTraFB5wEoImduF1qSzgMkNDU86q4POHfYNNfXxWfSQOGRRQ6Nt3HWAiDE50A3t7Zv/LJghaP9TPThjjv634Y25HhvMET4KfpDfQB358DSVJ30EU=',
            '__VIEWSTATEGENERATOR': '01AED449',
            '__VIEWSTATE': '/wEPDwUJNzE1NTUyMzU2D2QWAgIDDxYCHgdlbmN0eXBlBRNtdWx0aXBhcnQvZm9ybS1kYXRhFgwCAQ9kFgICBw8PFgIeBFRleHQFSSDZh9mIINin2YTZitmI2YUg2KfZhNiq2KfZhNmKINmE2KrYp9ix2YrYriDYqtiz2KzZitmE2YPZhSDYp9mKIDMwLzAzLzIwMjNkZAIGDxYCHgdWaXNpYmxlaGQCBw8WAh8CaGQCCA8WAh8CaGQCCQ8WAh8CaGQCCg8WAh8CaGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFCHJiRW50Sm9yBQhyYkV4dEpvclY09VFPpQzDZfGIqseDJ7h0WEqMBIkM5aAJOoEzRtFe',
            'gstdoc': file['الوجهة'][i],
            'txtName': file['الاسم'][i],
            'ddlNationality': file['الجنسية'][i],
            'txtPassportNu': file['رقم جواز السفر'][i],
            'txtIDNumber': file['الرقم الوطني'][i],
            'txtCarNumber': file['رقم السيارة'][i],
            'txtEmail': file['البريد الالكتروني'][i],
            'ddlCountryCode': "00"+str(file['رمز الدولة'][i]),
            'txtMobile': "0"+str(file['رقم الاتصال'][i]),
            'chAgreed3': 'true',
            'SubmitInvest': 'إرسال الطلب',
        }

        image_path = file['جواز السفر'][i] + '.jpg'
        files = {'hdFileUpload2': open(image_path, 'rb')}
        r = rq.post(url, headers=head, data=data, files=files)
        print(r)

def start():
    while True:
        now = datetime.datetime.now()
        if now.hour == 12 and 43 <= now.minute < 44:
            execute()
        




if __name__ == '__main__':
    start()
'''


