# HK_flag.py
from turtle import *
import math

def draw_hk_flag():
    # === 固定比例参数 ===
    H = 640                              # 区旗高度（可缩放）
    W = 1.5 * H                          # 长高比 3:2
    R_outer = (3/5) * H / 2              # 洋紫荆外圆半径 = 0.3H
    color_red = "#DE2910"                # 以中华人民共和国国旗红为标准

    setup(W + 100, H + 100)
    hideturtle()
    speed(0)
    title("Flag of the Hong Kong Special Administrative Region")

    # === 绘制旗面 ===
    fillcolor(color_red)
    pencolor(color_red)
    penup()
    goto(-W / 2, H / 2)
    pendown()
    begin_fill()
    for i in range(2):
        forward(W)
        right(90)
        forward(H)
        right(90)
    end_fill()

    # === 绘制紫荆花瓣 ===
    fillcolor("white")
    pencolor("white")

    n = 5
    angle_step = 360 / n

    for i in range(n):
        penup()
        goto(0, 0)
        seth(90 + i * 72)
        pendown()
        begin_fill()
        left(63)
        circle(-R_outer * 0.5, 144)
        right(145)
        circle(R_outer * 0.22, 80)
        circle(-R_outer * 0.22, 90)
        circle(R_outer * 0.25, 90)
        end_fill()

    # === 绘制红色花蕊与五角星 ===
    fillcolor(color_red)
    pencolor(color_red)

    for i in range(n):
        # 花瓣中心轴方向角度
        axis_angle = 90 + i * angle_step

        # 花蕊
        seth(axis_angle)
        penup()
        goto(0, 0)
        pendown()
        left(52)
        pensize(1)
        circle(-R_outer * 0.35, 80)
        pensize(1)
        penup()

        # 五星
        # 星心位于花瓣中心轴方向上，距中心约 R_outer * 0.50
        star_r = R_outer * 0.12
        star_center_dist = R_outer * 0.50

        star_x = star_center_dist * math.cos(math.radians(axis_angle))
        star_y = star_center_dist * math.sin(math.radians(axis_angle))

        # 小五星尖端朝向旗中心
        seth(towards(0, 0) - 90)
        goto(star_x, star_y)
        pendown()
        begin_fill()
        for j in range(5):
            forward(star_r)
            right(144)
        end_fill()
        penup()

    done()

if __name__ == "__main__":
    draw_hk_flag()