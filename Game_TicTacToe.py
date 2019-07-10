'''
Pygame Demo
(井字棋)
'''
import pygame
from pygame.locals import *

# 初始化
pygame.init()
# 设置窗体大小
screen = pygame.display.set_mode((600, 400))
# 背景颜色
screen.fill((255, 255, 255))
# 初始化游戏状态
running = True
# 保存棋子位置坐标集合
chess_locations = {(row, column): None for row in range(1, 4) for column in range(1, 4)}
# 棋盘坐标位置
chess_position_x, chess_position_y = 200, 150

# 增加文字
def show_text(text, position_x, position_y, text_height=48, font_color=(0, 0, 0), background_color=(255, 255, 255)):
    # 设置字体格式
    text_font = pygame.font.Font('Arial.ttf', text_height)
    # 设置显示的目标文字
    text_content = text_font.render(text, True, font_color, background_color)
    # 获取显示的目标载体
    text_location = text_content.get_rect()
    # 设置显示的坐标位置
    text_location.center = (position_x, position_y)
    # 将文字内容写到目标位置
    screen.blit(text_content, text_location)

# 判断胜负
def check_wining():
    winner = "u"
    for i in range(3):
        if chess_locations[(i+1, 1)] == chess_locations[(i+1, 2)] == chess_locations[(i+1, 3)] is not None:
            winner = chess_locations[(i+1, 1)]
            break
        if chess_locations[(1, i+1)] == chess_locations[(2, i+1)] == chess_locations[(3, i+1)] is not None:
            winner = chess_locations[(1, i+1)]
            break
    if chess_locations[(1, 1)] == chess_locations[(2, 2)] == chess_locations[(3, 3)] is not None:
        winner = chess_locations[(1, 1)]
    if chess_locations[(1, 3)] == chess_locations[(2, 2)] == chess_locations[(3, 1)] is not None:
        winner = chess_locations[(1, 3)]
    return winner

# 划线
def draw_line():
    # 起点坐标
    x_start, y_start = 0, 0
    # 终点坐标
    x_end, y_end = 0, 0
    for i in range(3):
        if chess_locations[(i+1, 1)] == chess_locations[(i+1, 2)] == chess_locations[(i+1, 3)] is not None:
            x_start, y_start = chess_position_x - 40, chess_position_y + (i)*64+37
            x_end, y_end = chess_position_x + 242, chess_position_y + (i)*64+37
            break
        if chess_locations[(1, i+1)] == chess_locations[(2, i+1)] == chess_locations[(3, i+1)] is not None:
            x_start, y_start = chess_position_x + (i)*64+37, chess_position_y - 40
            x_end, y_end = chess_position_x + (i)*64+37, chess_position_y + 242
            break
    if chess_locations[(1, 1)] == chess_locations[(2, 2)] == chess_locations[(3, 3)] is not None:
        x_start, y_start = chess_position_x - 40, chess_position_y - 40
        x_end, y_end = chess_position_x + 242, chess_position_y + 242
    if chess_locations[(1, 3)] == chess_locations[(2, 2)] == chess_locations[(3, 1)] is not None:
        x_start, y_start = chess_position_x - 20, chess_position_y + 222
        x_end, y_end = chess_position_x + 222, chess_position_y - 20
    # 划线(获胜路径)
    pygame.draw.line(screen, (255, 0, 0), (x_start, y_start), (x_end, y_end), 4)

# 落棋子到目标坐标
def put_chess(content, row, column):
    # 已有棋子
    if chess_locations[(row, column)] is not None:
        return False
    else:
        chess_locations[(row, column)] = content
        return True

# 画所有的棋子
def draw_chess():
    for (row, column) in chess_locations:
        chess(chess_locations[(row, column)], row, column)

#
def get_position(row, column):
    return chess_position_x + 37 + 64 * (column - 1), chess_position_y + 37 + 64 * (row - 1)

def position_verify(x, y):
    return (
        ((chess_position_x + 10 < x < chess_position_x + 10 + 54) + 2*(chess_position_x + 20 + 54 < x < chess_position_x + 20 + 2 * 54) + 3*(
                chess_position_x + 30 + 2 * 54 < x < chess_position_x + 30 + 3 * 54)),
        ((chess_position_y + 10 < y < chess_position_y + 10 + 54) + 2*(chess_position_y + 20 + 54 < y < chess_position_y + 20 + 2 * 54) + 3*(
                chess_position_y + 30 + 2 * 54 < y < chess_position_y + 30 + 3 * 54)))

# 棋盘
def chessboard(x, y):
    '''
　　用法: pygame.draw.rect(<target>, color, Rect, width=0): return Rect
　　理解: 在<target>上绘制矩形，第二个参数是线条（或填充）的颜色，第三个参数Rect的形式是((x, y), (width, height))，
            表示的是所绘制矩形的区域，其中第一个元组(x, y)表示的是该矩形左上角的坐标，
            第二个元组 (width, height)表示的是矩形的宽度和高度。
            width表示线条的粗细，单位为像素；默认值为0，表示填充矩形内部。
    '''
    # 底色
    pygame.draw.rect(screen, (0, 128, 0), Rect(x, y, 202, 202))
    # 单元格
    for i in range(9):
        pygame.draw.rect(screen, (255, 255, 255), Rect(x + 10 + (i % 3) * 64, y + 10 + (i // 3) * 64, 54, 54))

# 绘制棋子位置
def chess(content, row, column):
    if content == "o":
        # 绘制 O 图案
        pygame.draw.circle(screen, (0, 0, 0), get_position(row, column), 20, 3)
    elif content == "x":
        x, y = get_position(row, column)
        # 绘制 X 图案
        pygame.draw.line(screen, (0, 0, 0), (x - 18, y - 18), (x + 18, y + 18), 3)
        pygame.draw.line(screen, (0, 0, 0), (x + 18, y - 18), (x - 18, y + 18), 3)


i = 0
while running:
    # 1，判断执行游戏状态
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # 退出游戏
            if event.key == K_q:
                running = False
            # 重新开始
            if event.key == K_r:
                i = 0
                # 重新构建棋盘
                chess_locations = {(row, column): None for row in range(1, 4) for column in range(1, 4)}
                # show_text("The Game Ended In A Draw", 399, 100, 48, (255, 255, 255))
                pygame.draw.rect(screen, (255, 255, 255), (1, 1, 800, 600))
        if event.type == QUIT:
            running = False

    # 若鼠标点击，将棋落到chess_locations 数组(列表)
    cursor_x, cursor_y = pygame.mouse.get_pos()
    # 获取鼠标按钮的状态。
    # 当左键按下的时候btn_one 的值会被赋值为1，鼠标按键弹起是会被赋值为0。
    btn_one, btn_two, btn_three = pygame.mouse.get_pressed()
    show_content = "x"
    row, column = 1, 1
    if btn_one and i < 9:
        if i % 2 == 0:
            row, column = position_verify(cursor_x, cursor_y)
            show_content = "x"
        elif i % 2 == 1:
            row, column = position_verify(cursor_x, cursor_y)
            show_content = "o"
        if row == 0 or column == 0:
            continue
        if put_chess(show_content, column, row):
            i += 1

    # 画棋盘和棋子
    chessboard(chess_position_x, chess_position_y)
    show_text("'Q' -> Quit", 80, 20, 20)
    show_text("'R' -> Restart", 80, 50, 20)
    if check_wining() != "u":
        # 显示获胜信息
        show_text("[ "+check_wining()+" ] PASS", 340, 90)
        # 划线
        draw_line()
        i = 9
    elif i == 9 and check_wining() == "u":
        show_text("End In Tie", 340, 90)
    draw_chess()

    # 刷新
    pygame.display.update()
