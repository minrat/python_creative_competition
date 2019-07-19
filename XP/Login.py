import os
import json
from tkinter import *
from tkinter.messagebox import *

class Login(object):
    def __init__(self, master=None):
        self.root = master
        # 设置标题
        self.root.title("程序登录模块")
        # 设置框体
        self.root.geometry('600x400')
        # 单元框架
        self.frame_login = Frame(self.root)
        # 标签
        Label(self.frame_login, text="账号：").grid(row=0, column=0, columnspan=2)
        Label(self.frame_login, text="密码：").grid(row=1, column=0, columnspan=2)

        # 对话框
        self.entry_account = StringVar()
        Entry(self.frame_login, textvariable=self.entry_account).grid(row=0, column=5, columnspan=4)
        self.entry_password = StringVar()
        Entry(self.frame_login, textvariable=self.entry_password, show="*").grid(row=1, column=5, columnspan=4)

        # 复选框
        Checkbutton(self.frame_login, text="记录密码", onvalue=1, offvalue=0, height=5, width=10).grid(row=3, column=2, columnspan=2)
        Checkbutton(self.frame_login, text="自动登录", onvalue=1, offvalue=0, height=5, width=10).grid(row=3, column=6, columnspan=2)

        # 按钮
        Button(self.frame_login, text="登录", command=self.login).grid(row=5, column=3, columnspan=2)
        Button(self.frame_login, text="退出", command=self.root.quit).grid(row=5, column=6, columnspan=2)

        # 填充
        Label(self.frame_login, text="   ").grid(row=7, column=4, columnspan=2)
        Label(self.frame_login, text="   ").grid(row=8, column=4, columnspan=2)

        # 注册界面跳转
        Button(self.frame_login, text="没有账户？点我", command=self.start_register, fg="red", bg="yellow").grid(row=9, column=5, columnspan=2)

        # 组件打包
        self.frame_login.pack(side=TOP, expand=YES)
        self.root.mainloop()

    # 登录方法
    def login(self):
        print("Welcome Login")
        self.root.title("登录中，请稍后....")
        # 获取登录信息
        account = self.entry_account.get()
        password = self.entry_password.get()

        if account.strip() is "" or password.strip() is  "":
            showerror("错误", "用户密码不能为空")
        else:
            # 获取密码文件的信息(不为空情况下)
            token = self.get_login_info(account, password)

            # 比对&校验输入内容
            if token is True:
                print("登录成功")
                showinfo("成功", message="[" + str(account) + "] 登录成功")
                self.root.title("登录成功")

                # 登录成功.页面跳转
                self.login_pass()
            else:
                print("登录失败")
                showerror("失败", message="[" + str(password) + "] 登录失败（用户名或密码错误），请重试！")
                self.root.title(" 登录失败")

    # 登录成功
    def login_pass(self):
        # 登录界面销毁
        self.frame_login.destroy()

        # 功能界面引入
        from MainFrame import MainPage

        # 登录(将用户名带入)
        MainPage(self.root, self.entry_account.get())

    # 密码获取
    def get_login_info(self, username, password):
        flag = False
        # 获取文件夹
        path = os.getcwd()
        try:
            os.chdir(path + "/login_auth")
            # 查看文件
            f = open(path + "/login_auth/password.txt", "r")
            content = f.read()

            # 类型转换
            content = "{" + content[:-1] + "}"
            result_source = json.loads(content)

            # 用户校验(字典通过key获取value)
            if password == result_source.get(username):
               flag = True
        except OSError:
            # 信息框提示
            showerror("登录失败", "用户名或密码错误")
            print("用户不存在")
        return flag

    # 注册功能接入
    def start_register(self):
        # 登录信息注销(通过容器框架统一销毁)
        self.frame_login.destroy()

        # 引入register
        from Register import Register

        # 注册信息激活
        Register(self.root)