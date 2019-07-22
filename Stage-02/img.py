from tkinter import *
from PIL import ImageTk, Image


if __name__ == '__main__':

    root = Tk()

    # 背景图片设置
  
    img_path = 'img/flower.jpg'
    img = Image.open(img_path)
    photo = ImageTk.PhotoImage(img)
    
    frame = Frame(root)
    

    Button(frame, text="登录", image=photo).grid(row=1, column=3, columnspan=2)
    Button(frame, text="登录", image=photo).grid(row=2, column=3, columnspan=2)
    
    frame.pack()
    

    root.mainloop()
