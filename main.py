import pygame
import sys
file=r'C:\Users\LEGION\Music\秦岚 _ 江疏影 _ 景甜 _ 王俊凯 _ 王源 _ 易烊千玺 _ 吴磊 - 我们都是追梦人.mp3'
pygame.init()  # 初始化pygame
track = pygame.mixer.music.load(file)	# 加载音乐文件
pygame.mixer.music.play()				# 开始播放音乐流
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)  # 设置颜色
ball = pygame.image.load('ball.png')  # 加载图片
stop= pygame.image.load('暂停.png')
ballrect = ball.get_rect()  # 获取矩形区域
speed = [5, 5]  # 设置移动的X轴、Y轴
clock = pygame.time.Clock()  # 设置时钟

while True:  # 死循环确保窗口一直显示
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

    ballrect = ballrect.move(speed)  # 移动小球
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

        for event in pygame.event.get():
                if event.type == pygame.K_SPACE:
                  print(stop)

    screen.fill(color)
    screen.blit(ball, ballrect)
    pygame.display.flip()

pygame.quit()  # 退出pygame
