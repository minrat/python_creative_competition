import turtle

class Portrait(object):
    def __init__(self):
        # 设置画笔颜色
        turtle.pencolor("black")
        # pencolor=color1, fillcolor=color2
        # turtle.color("red", "yellow")
        # 设置画笔大小
        turtle.pensize(1)
        # 起笔
        turtle.penup()

    # 脸
    def face(self, face_type):
        print("开始画脸....")
        # 更改画笔粗细
        turtle.pensize(3)
        # 设置填充颜色
        turtle.fillcolor("blue")
        if face_type == "square":
            # 更改位置
            turtle.goto(-240, 220)
            # 落笔
            turtle.pendown()
            # 准备填充
            turtle.begin_fill()
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(400)
            # 填充结束
            turtle.end_fill()
            # 起笔
            turtle.penup()
        elif face_type == "circle":
            # 更改位置
            turtle.goto(-50, -150)
            # 落笔
            turtle.pendown()
            # 准备填充
            turtle.begin_fill()
            # 画圆
            turtle.circle(200, 360)
            # 填充结束
            turtle.end_fill()
            # 起笔
            turtle.penup()

    # 眉毛
    def eyebrow(self, eyebrow_type):
        pass

    # 眼睛
    def eye(self, eye_type):
        print("画眼睛....")
        if eye_type == "large":
            # 设置填充颜色
            turtle.fillcolor("red")
            # left eye
            turtle.goto(-100, 150)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(40, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

            # 眼睛中的黑色部分
            turtle.fillcolor("black")
            turtle.goto(-120, 150)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(15, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

            # right eye
            # 设置填充颜色
            turtle.fillcolor("red")
            # 光标移位
            turtle.goto(60, 150)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(40, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

            # right 眼睛中的黑色部分
            turtle.fillcolor("black")
            turtle.goto(40, 150)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(15, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

        elif eye_type == "small":
            # left eye
            # 设置填充颜色
            turtle.fillcolor("red")
            turtle.goto(-120, 140)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(20, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()
            # 眼球
            turtle.fillcolor("black")
            turtle.goto(-120, 150)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(4, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

            # right eye
            # 设置填充颜色
            turtle.fillcolor("red")
            turtle.goto(30, 150)
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(20, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

            # right 眼球
            turtle.fillcolor("black")
            turtle.goto(30, 155)
            # 准备填充
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(4, 360)
            # 填充结束
            turtle.end_fill()
            turtle.penup()

    # 鼻子
    def nose(self, nose_type):
        print("画鼻子.....")
        if nose_type == "":
            pass
        elif nose_type == "":
            pass

    # 嘴巴
    def mouth(self, mouth_type):
        pass

    # 头发
    def hair(self, hair_type):
        pass

    # 耳朵
    def ear(self, ear_type):
        pass

    # 完整画出肖像
    def full(self, face_type, eyebrow_type, eye_type, nose_type, mouth_type, hair_type, ear_type):
        self.face(face_type)
        self.eyebrow(eyebrow_type)
        self.eye(eye_type)
        self.nose(nose_type)
        self.mouth(mouth_type)
        self.hair(hair_type)
        self.ear(ear_type)


# if __name__ == '__main__':
#     p = Portrait()
#     p.full('square', 1, 'large', 1, 1, 1, 1)
#     # 后台循环
#     turtle.mainloop()
