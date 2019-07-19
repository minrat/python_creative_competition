import os
from tkinter import *
from tkinter.messagebox import *


# 注册界面
class Register(object):
    def __init__(self, master=None):
        self.root = master
        # 设置标题
        self.root.title("信息注册")
        # 设置框体
        self.root.geometry('600x400')
        # 单元框架
        self.frame_register = Frame(self.root)

        # 标签
        Label(self.frame_register, text="账    号：").grid(row=0, column=0, columnspan=2)
        Label(self.frame_register, text="密    码：").grid(row=1, column=0, columnspan=2)
        Label(self.frame_register, text="密码确认：").grid(row=2, column=0, columnspan=2)

        # 对话框
        self.entry_account = StringVar()
        Entry(self.frame_register, textvariable=self.entry_account).grid(row=0, column=5, columnspan=4)
        self.entry_password = StringVar()
        Entry(self.frame_register, textvariable=self.entry_password, show="*").grid(row=1, column=5, columnspan=4)
        self.entry_password_confirm = StringVar()
        Entry(self.frame_register, textvariable=self.entry_password_confirm, show="*").grid(row=2, column=5, columnspan=4)

        Label(self.frame_register, text="   ").grid(row=3, column=4, columnspan=2)
        Label(self.frame_register, text="   ").grid(row=4, column=4, columnspan=2)

        # 注册信息提交
        self.btn_commit = Button(self.frame_register, text="提交", command=self.do_register)
        self.btn_commit.grid(row=8, column=3, columnspan=2)

        # 页面返回跳转-登录页面
        Button(self.frame_register, text="返回", command=self.back_to_login).grid(row=8, column=6, columnspan=2)

        # 框体统一打包
        self.frame_register.pack(side=TOP, expand=YES)

        #
        self.root.mainloop()

    # 验证用户名是否存在
    # 通过函数返回值的不同,实现用户验证
    def user_check(self, user_name):
        flag = False
        # 文件只读打开
        f = open(os.getcwd() + "/login_auth/password.txt", "r")
        content = f.read()
        # 用户判断
        if user_name not in content:
            flag = True
        # 文件关闭
        f.close()
        return flag

    # 注册动作
    def do_register(self):
        # 禁用按钮
        self.btn_commit.config(state="disabled")

        # 信息获取
        register_username = self.entry_account.get()
        register_password = self.entry_password.get()
        register_password_confirm = self.entry_password_confirm.get()

        if register_username.strip() == "" or register_password.strip() == "" \
                or register_password_confirm.strip() == "":
            showerror("错误", message="用户名或密码不能为空，请确认输入！")
        else:
            if register_password != register_password_confirm:
                showerror("错误", message="两次密码不一致，请确认输入！")
            else:
                # 创建对应文件夹
                # 检查文件夹是否存在
                # os.access("/file/path/foo.txt", os.F_OK)
                path = os.getcwd()
                try:
                    os.chdir(path+"/login_auth")
                except OSError:
                    os.mkdir(path+"/login_auth")

                # 切换工作目录
                os.chdir(path)

                # 支持多用户,选择追加模式
                f = open(path+"/login_auth/password.txt", "a")

                # 多用户
                record = "\""+register_username+"\":\"" + register_password+"\""

                # 用户验证(接收用户验证的信息)
                user_status = self.user_check(register_username)

                # 用户不存在时
                if user_status is True:
                    # 写入文件内容
                    f.write(str(record)+",")
                    f.close()

                    # 信息框提示
                    showinfo("恭喜", message="[" + str(register_username) + "] 注册成功")
                else:
                    # 用户存在时
                    showerror("注册失败", "用户名已存在,请重新输入")

        # 启用按钮
        self.btn_commit.config(state="active")

    # 返回登录页面
    def back_to_login(self):
        # 注册页面销毁
        self.frame_register.destroy()

        # 登录页面引入
        from Login import Login

        # 登录页面激活
        Login(self.root)
