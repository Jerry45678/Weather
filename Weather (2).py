import requests
from bs4 import BeautifulSoup
import datetime

#天氣網站
url = "https://www.ttv.com.tw/news/weather/weekly.asp"


#取得網站資料
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64: x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(url, headers=headers, verify=False)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')

#尋找表格
table = soup.find('table', class_= 'table table-striped table-responsive')
#建立天氣和溫度空清單
weather = []
temperature = []
#從天氣圖標尋找
a = soup.find_all('img', class_='img-rounded WeatherCube')
#從表格中td尋找
b = soup.find_all('td')
#找圖片中的alt名字
for data in a:
    weather.append(data["alt"])
#找td中文字
for txt in b:
    temperature.append(txt.text)

#取得日期
days = []
for z in soup.find_all('font'):
    days.append(z.text)

#各地區天氣
Northw = []
Eastw = []
Southw = []
Westw = []
#用ljust可以限制字串長度
for n in range(0,7):
    Northw.append(weather[n+7].ljust(12,'　'))
    Eastw.append(weather[n+14].ljust(12,'　'))
    Southw.append(weather[n+21].ljust(12,'　'))
    Westw.append(weather[n+28].ljust(12,'　'))

#各地區溫度
Northt = []
Eastt = []
Southt = []
Westt = []
for n in range(2,9):
    Northt.append("溫度：")
    Northt.append(temperature[n+7].ljust(18,' '))
    Eastt.append("溫度：")
    Eastt.append(temperature[n+15].ljust(18,' '))
    Southt.append("溫度：")
    Southt.append(temperature[n+23].ljust(18,' '))
    Westt.append("溫度：")
    Westt.append(temperature[n+31].ljust(18,' '))

#排版 & 匯出結果
count = 0
weekname = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
w = []
#確認今天是星期幾
firstday = datetime.datetime.now().isoweekday()
count1 = firstday - 1
#排列本周順序
for c in range(7):
    w.append(weekname[count1])
    count1+=1
    if count1 > 6:
        count1-=7
week = w[0]+"                  "+w[1]+"                  "+w[2]+"                  "+w[3]+"                  "+w[4]+"                  "+w[5]+"                  "+w[6]
City = ['北部地區   ','中部地區   ','南部地區   ','東部地區   ']
Area = [Northw,Eastw,Southw,Westw]
temper = [Northt,Eastt,Southt,Westt]
print("                                                                     本週天氣","(",days[0],"~",days[-1],")")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for x in range(0,4):
    print(City[count],week)
    print('　　　　   ',"".join(Area[x]))
    print('　　　　   ',"".join(temper[x]))
    print()
    count+=1

#目前不支援存檔功能