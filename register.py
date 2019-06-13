'''
说明： 注册的时候，将注册信息写入文件
'''
import os
from tkinter import *
from tkinter.messagebox import *

# 注册界面
class Register:
    def __init__(self):
        register = Tk()
        # 设置标题
        register.title("信息注册")
        # 设置框体
        register.geometry('600x400')
        # 单元框架
        frame_1 = Frame(register)

        # 标签
        Label(frame_1, text="账    号：").grid(row=0, column=0, columnspan=2)
        Label(frame_1, text="密    码：").grid(row=1, column=0, columnspan=2)
        Label(frame_1, text="密码确认：").grid(row=2, column=0, columnspan=2)

        # 对话框
        self.entry_account = StringVar()
        Entry(frame_1, textvariable=self.entry_account).grid(row=0, column=5, columnspan=4)
        self.entry_password = StringVar()
        Entry(frame_1, textvariable=self.entry_password, show="*").grid(row=1, column=5, columnspan=4)
        self.entry_password_confirm = StringVar()
        Entry(frame_1, textvariable=self.entry_password_confirm, show="*").grid(row=2, column=5, columnspan=4)

        # 按钮
        self.btn_commit = Button(frame_1, text="提交", command=self.do_register)
        self.btn_commit.grid(row=5, column=3, columnspan=2)
        Button(frame_1, text="返回", command=register.quit).grid(row=5, column=6, columnspan=2)

        frame_1.pack()
        register.mainloop()

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
                try:
                    os.chdir("login_auth")
                except OSError:
                    os.mkdir("login_auth")
                    os.chdir("login_auth")

                # 执行文件生成
                f = open("password.txt", "w+")

                record = {"username": register_username, "password": register_password}

                # 写入文件内容
                f.write(str(record))

                # 查看文件
                f = open("password.txt", "r")
                content = f.read()
                print(content)
                f.close()
                showinfo("恭喜", message="[" + str(register_username) + "] 注册成功")

        # 启用按钮
        self.btn_commit.config(state="active")


if __name__ == '__main__':
    r = Register()
