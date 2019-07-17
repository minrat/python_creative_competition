# -*- coding: utf-8 -*-

'''
使用说明：
    仅需要更改查询目标地名称
'''

import json
import urllib.request

class Weather:
    def __init__(self):
        # 初始化
        self.url = "http://api.map.baidu.com/telematics/v3/weather?output=json&"
        self.ak = "A5CGqctY5c0RwTfZFuktytfw"

    def getWeather(self, city):
        url = self.url + 'location=' + urllib.parse.quote(city) + '&ak=' + self.ak
        response = urllib.request.urlopen(url).read()
        result = response.decode('utf-8')
        result = json.loads(result)
        # 查询返回日期
        date = result.get('date')
        print("日 期："+date)
        result = dict(result['results'][0])
        # city
        city = result.get('currentCity')
        print("城 市： "+city)
        # pm25
        pm25 = result.get('pm25')
        print("PM2.5： "+pm25)

        # advice
        tips = []
        advice = result.get('index')
        for i in range(0, len(advice)-1):
            # 意见
            suggestion = advice[i].get('des')
            tips.append(suggestion)

        # weather detail
        detail = []
        weather = result.get('weather_data')
        for i in range(0, len(weather)-1):
            detail.append(weather[i].get('date') + " | "+weather[i].get('weather') + " | "+weather[i].get('wind') + " | " +weather[i].get('temperature'))

        print("详 情： "+str(detail))
        print("贴 士： "+str(tips))


if __name__ == '__main__':
    # 根据需要更改
    city = "上海"
    w = Weather()
    w.getWeather(city=city)
