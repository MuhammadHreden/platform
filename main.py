import asyncio
from pyppeteer import launch
import pandas as pd
import datetime


async def execute():
   file = pd.read_csv(r'final.csv', header=0)
   browserObj = await launch(headless=False)#{"headless": True, "args" : ['--no-sandbox', '--disable-setuid-sandbox'] , "ignoreDefaultArgs" : ['--disable-extensions'] } )
   url = await browserObj.newPage()
   url.waitFor(9000000000000000000000)
   while True:
      now = datetime.datetime.now()
      if now.minute > 10 and now.minute <50:
         break
   for i in range(len(file.index)):
      await url.goto('https://visitjordan.gov.jo/travelcars/')
      await url.evaluate('''() => {
                 let radio = document.querySelector('#rbEntJor');
                 radio.click();
             }''')
      await url.type("#txtName", file['الاسم'][i])
      await url.select('[id=ddlNationality]', "192")
      await url.type("#txtPassportNu", file['رقم جواز السفر'][i])
      await url.type("#txtIDNumber", file['الرقم الوطني'][i].astype(str))
      await url.type("#txtCarNumber", file['رقم السيارة'][i].astype(str))
      await url.type("#txtEmail", file['البريد الالكتروني'][i])
      await url.select('[id=ddlCountryCode]', "00963")
      await url.type("#txtMobile", "0954143723")
      input_file = await url.querySelector('[id=FileUpload2]')
      file_path = file['جواز السفر'][i] + '.jpg'
      await input_file.uploadFile(file_path)
      await url.click('body > form > section > div > div > div > div > div > div > input.checkboxbtn')
      await url.click('body > form > section > div > div > div > div > div > input.cbtn')
      url = await browserObj.newPage()

   await browserObj.close()


def start():

   while True:
      now = datetime.datetime.now()
      if (now.hour == 0 and 59 <= now.minute < 60) or (now.hour == 1 and 0 <= now.minute < 5):
         try:
            asyncio.get_event_loop().run_until_complete(execute())
         except Exception:
            pass




if __name__ == '__main__':
     start()