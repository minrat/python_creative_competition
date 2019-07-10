'''
注意&思考 字符拼接的场景
'''
# Diamond
def character(ch, width):
    print("实心菱形")
    for i in range(1, width+1, 1):
        print(" "*(width - (i - 1)) + ch * (2 * i - 1))

    for j in range(width-1, 0, -1):
        print(" "*(width - (j - 1)) + ch * (2*j - 1))

    print("空心菱形")
    for i in range(1, width+1, 1):
        if i > 1 and i <= width:
            print(" " * (width - (i - 1)) + ch+" "*(2*i - 2) + ch)
        else:
            print(" "*(width - (i - 1)) + ch * (2 * i - 1))

    for j in range(width-1, 0, -1):
        if j > 1 and j <= width -1:
            print(" "*(width - (j - 1)) + ch + (2*j - 2)*" " + ch)
        else:
            print(" " * (width - (j - 1)) + ch * (2 * j - 1))

# Triangle
def triangle(ch, width):
    print("实心三角形")
    # 实心
    for i in range(1, width+1):
        print((2*i -1)*ch)

    print("空心三角形")
    # 空心
    for j in range(1, width+1):
        if j == 1 or j == width:
            print((2*j - 1) * ch)
        else:
            print(ch + " "*(2*j - 2) + ch)

# Rectangle
def rectangle(ch, width):
    print("实心长方形")
    # 实心
    for i in range(1, width, 2):
        print(width*(ch+"\t"))

    # 空心
    print("空心长方形")
    for i in range(1, width+1, 2):
        if i == 1 or i == width or i == width-1:
            print(width*(ch+"\t"))
        else:
            print(ch +(width-1)*"\t"+ch)


# Square
def square(ch, width):
    print("实心正方形")
    # 实心
    for i in range(1, width, 1):
        print(int(width)*(ch+"\t"))

    # 空心
    print("空心正方形")
    for j in range(1, width+1, 1):
        if j == 1:
            print(int(width) * (ch + "\t"))
        elif 1 < j and j < width:
            print(ch + (width-1)*"\t"+ ch)
        elif j == width:
            print(int(width) * (ch + "\t"))


if __name__ == '__main__':
    # 菱形
    character("*", 5)
    # 三角形
    triangle("*", 6)
    # 正方形
    square("*", 6)
    # 长方形
    rectangle("*", 6)
    
  # 结果如下
  '''
    ------------------------
    实心菱形
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
空心菱形
     *
    *  *
   *    *
  *      *
 *        *
  *      *
   *    *
    *  *
     *
实心三角形
*
***
*****
*******
*********
***********
空心三角形
*
*  *
*    *
*      *
*        *
***********
实心正方形
*	*	*	*	*	*	
*	*	*	*	*	*	
*	*	*	*	*	*	
*	*	*	*	*	*	
*	*	*	*	*	*	
空心正方形
*	*	*	*	*	*	
*					*
*					*
*					*
*					*
*	*	*	*	*	*	
实心长方形
*	*	*	*	*	*	
*	*	*	*	*	*	
*	*	*	*	*	*	
空心长方形
*	*	*	*	*	*	
*					*
*	*	*	*	*	*	
    ------------------------
    '''
