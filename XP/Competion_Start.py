from tkinter import *
from Login import *

if __name__ == '__main__':
    root = Tk()
    root.title('创意-作品演示')
    # 激活登录
    login = Login(root)
    root.mainloop()