from enum import Enum, unique
from random import randint
from math import sqrt
import pygame
import tkinter
import tkinter.messagebox


def screen():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', "Hello World") if flag else (
            'Blue', "Good, world!")
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("溫馨提示", "確定要退出嗎？"):
            top.quit()

    # 建立頂層視窗
    top = tkinter.Tk()
    top.geometry('540x360')
    top.title('小遊戲')
    # 建立 label，並加到頂層的視窗
    label = tkinter.Label(top, text="Hello World!", font="Arial -32", fg="red")
    label.pack(expand=1)
    # 建立一個裝按鈕的容器
    panel = tkinter.Frame(top)
    # 建立鍵鈕，並加至 畫面
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side="left")
    button2 = tkinter.Button(panel, text="退出", command=confirm_to_quit)
    button2.pack(side="right")
    panel.pack(side="bottom")
    # 建立主事件的循環
    # GUI 通常是事件驅動， mainloop() 的主要目的，就是監聰鍵盤、滑鼠
    # 並針對事件做回應
    tkinter.mainloop()


# @unique
# class Color(Enum):
#     RED = (255, 0, 0)
#     BLUE = (0, 0, 255)
#     GREEN = (0, 255, 0)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GRAY = (242, 242, 242)
#     @staticmethod
#     def random_color():
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         return (r, g, b)


# class Ball(object):
#     def __init__(self, x, y, radius, sx, sy, color=Color.RED):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True

#     def move(self, screen):
#         self.x += self.sx
#         self.y += self.sy
#         if self.x - self.radius <= 0 or \
#                 self.x+self.radius >= screen.get_width():
#             self.sx = -self.sx
#         if self.y - self.radius <= 0 or \
#                 self.y + self.radius >= screen.get_height():
#             self.sy = -self.sy

#     def eat(self, other):
#         if self.alive and other.alive and self != other:
#             dx, dy = self.x-other.x, self.y-other.y
#             distance = squrt(dx**2+dy**2)
#             if distance < self.radius + other.radius \
#                     and self.radius > other.radius:
#                 other.alive = False
#                 self.radius = self.radius+int(other.radius * 0.146)

#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color,
#                            (self.x, self.y), self.radius, 0)


# def game():
#     balls = []
#     # 初始化
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("大球吃小球")
#     # # 設置背景色
#     # screen.fill((255, 255, 255))
#     '''
#     draw 圖形
#     '''
#     # # 繪圓形 (screen, color, center posistion,radius, 0 填充圓)
#     # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
#     # 路徑的設置要從專案的根目錄開始
#     '''
#     圖形讀入
#     '''
#     # ball_image = pygame.image.load('Day01-15/pratice_code/ball.png')
#     # # screen.blit ( 圖片， (中心點位置) )
#     # screen.blit(ball_image, (50, 50))
#     # # refresh to show the drawing or image
#     # pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == game.MOUSEBUTTONDOWN and \
#                     event.button == 1:
#                 x, y = event.pos
#                 radius = randint(10, 100)
#                 sx, sy = randint(-10, 10), randint(-10, 10)
#                 color = Color.random_color()
#                 # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
#                 ball = Ball(x, y, radius, sx, sy, color)
#                 # 将球添加到列表容器中
#                 balls.append(ball)
#         screen.fill((255, 255, 255))
#         # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)
#             else:
#                 balls.remove(ball)
#         pygame.display.flip()
#         # 每隔50毫秒就改变球的位置再刷新窗口
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             # 检查球有没有吃到其他的球
#             for other in balls:
#                 ball.eat(other)

#         # screen.fill((255, 255, 255))
#         # pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
#         # pygame.display.flip()
#         # pygame.time.delay(50)
#         # x, y = x+5, y+5

@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def game():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == "__main__":
    game()
