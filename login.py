import os
from tkinter import *
from tkinter.messagebox import *

class Login():
    def __init__(self, root):
        # root = Tk()
        # 设置标题
        # self.root.title("程序登录")
        # 设置框体
        root.geometry('600x400')
        # 单元框架
        frame_1 = Frame(root)
        # 标签
        Label(frame_1, text="账号：").grid(row=0, column=0, columnspan=2)
        Label(frame_1, text="密码：").grid(row=1, column=0, columnspan=2)

        # 对话框
        entry_account = StringVar()
        Entry(frame_1, textvariable=entry_account).grid(row=0, column=5, columnspan=4)
        entry_password = StringVar()
        Entry(frame_1, textvariable=entry_password, show="*").grid(row=1, column=5, columnspan=4)

        # 复选框
        Checkbutton(frame_1, text="记录密码", onvalue=1, offvalue=0, height=5, width=10).grid(row=3, column=2, columnspan=2)
        Checkbutton(frame_1, text="自动登录", onvalue=1, offvalue=0, height=5, width=10).grid(row=3, column=6, columnspan=2)

        # 密码获取
        def get_login_info(username, password):
            flag = False
            # 创建对应文件夹
            try:
                os.chdir("login_auth")
                # 查看文件
                f = open("password.txt", "r")
                content = f.read()
                if username in content and password in content:
                    flag = True
            except OSError:
                print("不存在")
            return flag

        # 登录方法
        def login():
            print("Welcome Login")
            root.title("登录中，请稍后....")
            # 获取登录信息
            account = entry_account.get()
            password = entry_password.get()

            # 获取密码文件的信息
            token = get_login_info(account, password)

            # 比对&校验输入内容
            if token == True:
                print("登录成功")
                showinfo("成功", message="["+str(account)+"] 登录成功")
                root.title("登录成功")

            else:
                print("登录失败")
                showerror("失败", message="["+str(password)+"] 登录失败（用户名或密码错误），请重试！")
                root.title(" 登录失败")

        # 按钮
        Button(frame_1, text="登录", command=login).grid(row=5, column=3, columnspan=2)
        Button(frame_1, text="退出", command=root.quit).grid(row=5, column=6, columnspan=2)

        Label(frame_1, text="").grid(row=6, column=5, columnspan=2)
        Label(frame_1, text="").grid(row=7, column=5, columnspan=2)
        # Button(frame_1, text="没有账户？请点击我",).grid(row=8, column=4, columnspan=2)

        # 组件打包
        frame_1.pack(side=TOP, expand=YES)
        root.mainloop()
