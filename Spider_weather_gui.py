# -*- coding: utf-8 -*-

'''
使用说明：
    仅需要更改查询目标地名称
'''

import json
from tkinter import *
from tkinter.messagebox import *
import urllib.request

class Weather:
    def __init__(self):
        # 初始化
        root = Tk()
        # 设置标题
        root.title("中国天气预报")
        # 设置框体
        root.geometry('600x400')
        # 单元框架
        frame_1 = Frame(root)

        # 标签
        Label(frame_1, text="城市名称：").grid(row=0, column=0, columnspan=2)
        # 必填项标志(前景色,背景色)
        Label(frame_1, text="( * ,必填,如:上海)", bg='#FFFF00', fg='#FF0000').grid(row=0, column=10, columnspan=2)
        Label(frame_1, text="当前日期：").grid(row=1, column=0, columnspan=2)
        Label(frame_1, text="PM 2.5：").grid(row=2, column=0, columnspan=2)
        Label(frame_1, text="天气详情：").grid(row=3, column=0, columnspan=2)
        Label(frame_1, text="贴 士：").grid(row=4, column=0, columnspan=2)

        # 对话框:城市名称
        self.entry_city = StringVar()
        Entry(frame_1, textvariable=self.entry_city).grid(row=0, column=5, columnspan=4)

        # 对话框:当前日期
        self.entry_date = StringVar()
        self.date = Entry(frame_1, textvariable=self.entry_date)
        self.date.config(state="disabled")
        self.date.grid(row=1, column=5, columnspan=4)

        # 对话框:PM2.5
        self.entry_pm25 = StringVar()
        self.pm25 = Entry(frame_1, textvariable=self.entry_pm25)
        self.pm25.config(state="disabled")
        self.pm25.grid(row=2, column=5, columnspan=4)

        # 对话框:天气详情
        self.entry_weather_detail = Text(frame_1, width=20, height=10)
        self.entry_weather_detail.config(state="normal")
        self.entry_weather_detail.grid(row=3, column=5, columnspan=4)

        # 对话框:贴士
        self.entry_tips = Text(frame_1, width=20, height=10)
        self.entry_tips.config(state="normal")
        self.entry_tips.grid(row=4, column=5, columnspan=4)

        # 确认按钮
        self.button_commit = Button(frame_1, text="查询", command=self.get_weather_detail).grid(row=5, column=5, columnspan=4)

        # 框体容器统一打包至窗体对象
        frame_1.pack()

        # 使用百度提供的天气预报接口
        self.url = "http://api.map.baidu.com/telematics/v3/weather?output=json&"
        self.ak = "A5CGqctY5c0RwTfZFuktytfw"

        root.mainloop()

    def get_weather_detail(self):
        # 获取城市名称
        city = self.entry_city.get()
        # 开始处理结果
        if city.strip() == "":
            showerror("错误", "城市名称不能为空")
        else:
            url = self.url + 'location=' + urllib.parse.quote(city) + '&ak=' + self.ak
            response = urllib.request.urlopen(url).read()
            result = response.decode('utf-8')
            result = json.loads(result)

            # 查询返回日期
            date = result.get('date')
            self.entry_date.set(date)
            print("日 期："+date)
            result = dict(result['results'][0])

            # city
            city = result.get('currentCity')
            print("城 市： "+city)

            # pm25
            pm25 = result.get('pm25')
            self.entry_pm25.set(pm25)
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
                detail.append(weather[i].get('date') + " | " + weather[i].get('weather') +
                             " | " + weather[i].get('wind') + " | " + weather[i].get('temperature'))

            # 天气信息详情返回
            self.entry_weather_detail.insert(INSERT, str(detail))
            print("详 情： "+str(detail))
            # 贴士信息返回
            self.entry_tips.insert(INSERT, str(tips))
            print("贴 士： "+str(tips))

if __name__ == '__main__':

    w = Weather()
