from tkinter import *

'''
程序主界面需要根据个人喜好美化一下
'''

class MainPage(object):
    def __init__(self, master=None, user_account=None):
        self.root = master
        # 设置标题
        self.root.title("程序功能选择")
        # 设置框体
        self.root.geometry('600x400')
        # 单元框架
        self.frame_main = Frame(self.root)

        # 显示用户
        Label(self.frame_main, text="欢迎您,[ "+user_account+" ]").grid(row=1, column=0, columnspan=2)
        # 记录用户名
        self.username = user_account

        # 菜单按钮
        Button(self.frame_main, text="趣味画像", command=self.go_question_paint).grid(row=5, column=3, columnspan=2)

        Button(self.frame_main, text="游戏天地", command=self.go_game_ball).grid(row=8, column=3, columnspan=2)

        self.frame_main.pack(anchor=W)

    # 趣味画像
    def go_question_paint(self):
        # 功能销毁
        self.frame_main.destroy()
        # 引入问卷
        from Questionnaire import Questionnaire
        Questionnaire(self.root, self.username)

    # 游戏天地
    def go_game_ball(self):
        # 游戏引入
        from CatchBall import Ball
        # 游戏开始
        ball = Ball(self.username)
        ball.start_game()