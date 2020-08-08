import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *

class QRTool():
    # def __init__(self, root):
    def __init__(self):
        root = Tk()
        # 设置标题
        root.title("二维码制作")
        # 设置框体
        root.geometry('600x400')
        # 单元框架
        frame_1 = Frame(root)
        # 标签
        Label(frame_1, text="日期：").grid(row=0, column=0, columnspan=2)
        Label(frame_1, text="主题：").grid(row=1, column=0, columnspan=2)
        Label(frame_1, text="内容：").grid(row=2, column=0, columnspan=2)
        Label(frame_1, text="二维码:").grid(row=3, column=0, columnspan=2)

        # 对话框
        entry_date = StringVar()
        Entry(frame_1, textvariable=entry_date).grid(row=0, column=5, sticky=W)

        entry_title = StringVar()
        Entry(frame_1, textvariable=entry_title).grid(row=1, column=5, sticky=W)

        entry_content = Text(frame_1, height=6)
        entry_content.grid(row=2, column=5, sticky=W)

        # 图片显示区域
        self.img = ""
        self.canvas = Label(frame_1, text="....", image=self.img)
        self.canvas.grid(row=3, column=5, sticky=W)

        # 二维码生成方法
        def generate():
            print("Welcome QRcode")
            root.title("生成中，请稍后....")
            # 获取登录信息
            content_date = entry_date.get()
            content_title = entry_title.get()
            content = entry_content.get('0.0', 'end')

            if content_date == "" or content_title == "" or content == "":
                print("Invalid Information, Please Double Confirm!!")
                showerror("失败", message="生成失败（【时间】或【标题】或【内容】为空），请重试！")
            else:
                # 预处理二维码生成的信息
                content = content_date+content_title+content
                result = self.qr_generate(content)

                # 校验生成结果
                if result == 1:
                    print("生成成功")
                    showinfo("成功", message="[二维码 生成成功]")
                    # 更新标题
                    root.title("生成成功")

                else:
                    print("生成失败")
                    showerror("失败", message="[二维码 生成失败]，请重试！")
                    # 更新标题
                    root.title(" 生成失败")

        # 按钮
        Button(frame_1, text="返回", command=root.quit).grid(row=10, column=3, sticky=W)
        Button(frame_1, text="生成", command=generate).grid(row=10, column=5, sticky=W)

        # 组件打包
        frame_1.pack(side=TOP, expand=YES)
        root.mainloop()

    # 信息处理
    def qr_generate(self, content):
        # 标志位设定
        flag = 0
        # qrcode 工具的标准用法
        import qrcode
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        # 待转换内容填充
        qr.add_data(content.encode("utf-8"))
        # 生成
        qr.make(fit=True)
        img = qr.make_image()

        # 保存图片
        try:
            img.save('qrcode.png')
            img_read = Image.open('qrcode.png')
            image_file = ImageTk.PhotoImage(img_read)
            # 加载显示
            self.img = image_file
            self.canvas.configure(image=self.img)
            self.canvas.update()
            # 更新标志位
            flag = 1
        except OSError:
            print("不存在")
            # 更新标志位
            flag = 0

        return flag


if __name__ == '__main__':
    qr = QRTool()
