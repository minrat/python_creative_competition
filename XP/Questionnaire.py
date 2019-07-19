'''
问卷调查，可以根据实际需求，重新设计问卷

[可以根据实际需要更改问题以及选项]

'''

from tkinter import *
from tkinter.messagebox import *

class Questionnaire(object):
    def __init__(self, master=None, username=None):
        self.root = master
        self.root.geometry('600x400')
        self.root.maxsize(800, 600)
        self.root.title("趣味竞赛-问答篇")
        # 框体构建
        self.frame_question = Frame(self.root)
        self.page = 0

        # 用户名记录
        self.username = username

        # 用户名显示,可修改
        self.label_username = Label(self.frame_question, text="欢迎你,[ "+self.username+" ]", justify=RIGHT, fg="green")
        self.label_username.pack(anchor=E)

        # 确定使用StringVar 类型
        self.option_chose = StringVar()

        # 问题集合
        self.question_title_list = [
                             "1、你期望的是什么 [脸型]？ ",
                             "2、你期望的是什么样的 [眼睛]？",
                             "3、你期望的是什么样的 [鼻子]？",
                             "4、你期望的是什么样的 [嘴巴]？",
                             "5、你期望的是什么样的 [头发]？",
                             "6、你期望的是什么样的 [耳朵]？",
                             "7、你期望的是什么样的 [眉毛]？"
                             ]

        # 选项集合
        self.answer_option_list = [
            ["A、方形脸", "B、圆形脸"],
            ["A、铜铃眼", "B、芝麻眼"],
            ["A、平实鼻", "B、塌梁鼻"],
            ["A、嘟嘟嘴", "B、椭形嘴"],
            ["A、波形发", "B、直发"],
            ["A、招风耳", "B、无耳垂"],
            ["A、柳叶眉", "B、拱形眉"]
        ]

        # 定义一个可以存放结果的列表
        self.result = []

        # 问题设置
        # justify=LEFT, 字符串左对齐
        self.label_title = Label(self.frame_question, text=self.question_title_list[self.page], justify=LEFT, padx=20)
        self.label_title.pack(anchor=W)

        # 选项设置
        # anchor 对齐方式，左对齐"W"，右对齐"E"，顶对齐"N",默认居中对齐
        # 第一选项
        self.item_a = Radiobutton(self.frame_question, text=self.answer_option_list[self.page][0], padx=20,
                                  variable=self.option_chose, val=self.answer_option_list[self.page][0])
        self.item_a.pack(anchor=W)

        # 第二选项
        self.item_b = Radiobutton(self.frame_question, text=self.answer_option_list[self.page][1], padx=20,
                                  variable=self.option_chose, val=self.answer_option_list[self.page][1])
        self.item_b.pack(anchor=W)

        # 翻页(向后)按钮
        self.button_previous = Button(self.frame_question, text="上一页", command=self.go_previous_page)
        self.button_previous.pack()

        # 翻页(向前)按钮
        self.button_next = Button(self.frame_question, text="下一页", command=self.go_next_page)
        self.button_next.pack()

        # 提交按钮
        self.button_submit = Button(self.frame_question, text="提交", command=self.submit)

        # 框体打包
        self.frame_question.pack()

        mainloop()

    # 获取选择结果
    def get_choice_result(self):
        # 将获取的值写入列表
        self.result.append(self.option_chose.get())

    # 处理提交按钮动作
    def submit(self):
        # 获取当前选择结果
        self.get_choice_result()

        # 判断所有问题,是否有未选择
        if "" in self.result:
            # 如有未选择的,发出警告信息
            showwarning("【请注意】", message="你有未选择的画像属性！")
        else:
            # 销毁问题及选项（组件）
            self.label_title.destroy()
            self.item_a.destroy()
            self.item_b.destroy()

            # 销毁按钮
            self.button_previous.destroy()
            self.button_submit.destroy()

            # 根据得分，条件适配
            label = Label(self.frame_question, text="素描结果 :")
            label.pack()

            message = Label(self.frame_question, text=self.result)
            message.pack()

            # 画图
            paint_button = Button(self.frame_question, text="肖像确认", command=self.paint_portrait, fg="red", bg="yellow")
            paint_button.pack()

            # 返回主界面
            back_button = Button(self.frame_question, text="返回主界面", command=self.back_home)
            back_button.pack()

    # 返回主界面
    def back_home(self):
        # 销毁问卷
        self.frame_question.destroy()

        # 启用主功能
        from MainFrame import MainPage
        # 激活(需要带用户名)
        MainPage(self.root, self.username)

    # 向后翻页
    def go_previous_page(self):
        if self.page >= 1:
            # 页面编号自检
            self.page -= 1

            # 将已经存放的结果释放
            self.result.pop()

            # 重新启用翻页功能
            if self.page <= len(self.question_title_list) - 1:

                # 销毁提交按钮
                self.button_submit.destroy()

                # 获取按钮的状态,如果未启用,则启用
                if self.button_next.winfo_exists() == 0:
                    self.button_next = Button(self.root, text="下一页", command=self.go_next_page)
                    self.button_next.pack()

            # 页面跳转的时候,设置RadioButton 的标题
            self.label_title["text"] = self.question_title_list[self.page]
            # 设置选项的文本标题
            self.item_a["text"] = self.answer_option_list[self.page][0]
            # 设置选项的变量
            self.item_a["val"] = self.answer_option_list[self.page][0]

            self.item_b["text"] = self.answer_option_list[self.page][1]
            self.item_b["val"] = self.answer_option_list[self.page][1]

    # 向前翻页
    def go_next_page(self):
        if self.page < len(self.question_title_list)-1:

            # 获取当前选择结果
            self.get_choice_result()

            # 页面增加
            self.page += 1

            # 判断是否页面跳转到最后一页
            if self.page == len(self.question_title_list) - 1:
                # 获取选项结果
                self.get_choice_result()

                # 销毁下一页按钮
                self.button_next.destroy()

                # 启用提交按钮
                self.button_submit = Button(self.root, text="提交", command=self.submit)

                # 按钮打包到主窗体
                self.button_submit.pack()

            self.label_title["text"] = self.question_title_list[self.page]

            self.item_a["text"] = self.answer_option_list[self.page][0]
            self.item_a["val"] = self.answer_option_list[self.page][0]

            self.item_b["text"] = self.answer_option_list[self.page][1]
            self.item_b["val"] = self.answer_option_list[self.page][1]

    def paint_portrait(self):
        print("开始画图")
        # 引入画图
        from Portrait import Portrait
        p = Portrait()
        # 问卷选择结果
        # eye =
        # bizi =
        # mouth =
        # .....

        # 执行画图
        p.full('square', 1, 'large', 1, 1, 1, 1)