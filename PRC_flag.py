# PRC_flag.py
from turtle import *
import math

def draw_star_polygon(center_x, center_y, outer_r, rotation_deg, fill_color):
    """在(center_x,center_y)绘制外接圆半径outer_r的五角星，
       rotation_deg 指定第一个外顶点角度（度），逆时针为正。
       使用五角星连接顺序 0->2->4->1->3->0。"""
    # 计算外顶点（5个）
    pts = []
    for k in range(5):
        theta = math.radians(rotation_deg + k * 72)
        x = center_x + outer_r * math.cos(theta)
        y = center_y + outer_r * math.sin(theta)
        pts.append((x, y))
    order = [0, 2, 4, 1, 3, 0]
    penup()
    goto(pts[order[0]])
    pendown()
    color(fill_color)
    begin_fill()
    for idx in order[1:]:
        goto(pts[idx])
    end_fill()
    penup()

def draw_china_flag():
    # 旗面参数
    H = 600.0               # 旗高，可调整以缩放
    W = 1.5 * H             # 旗宽 = 3/2 H
    big_d = 0.30 * H        # 大星直径 = 0.3 H
    small_d = 0.10 * H      # 小星直径 = 0.1 H
    big_r = big_d / 2.0
    small_r = small_d / 2.0

    # 创建窗口与坐标系（将旗面置于中心）
    setup(int(W + 80), int(H + 80))
    speed(0)
    title("Flag of the People's Republic of China")
    bgcolor("#DE2910")      # 国旗红
    # 将坐标系置于以窗口中心为原点，便于使用上/下左右坐标
    setworldcoordinates(-W/2, -H/2, W/2, H/2)

    # 大星中心（距离左上角0.25H,0.25H）
    # 左上角在坐标系中为 (-W/2, H/2)
    big_cx = -W/2 + 0.25 * H
    big_cy = H/2 - 0.25 * H

    # 大星颜色（标准黄）
    star_yellow = "#FFDE00"

    # 画大星：设置第一个外顶点朝向90°（即一尖朝向正上方）
    draw_star_polygon(big_cx, big_cy, big_r, 90, star_yellow)

    # 小星中心（使用国家标准定位，坐标以左上角为基准）
    # 给出的4组 (dx, dy) 表示从左上角向右、向下的距离（单位：H）
    small_positions_H_units = [
        (0.50 * H, 0.10 * H),
        (0.60 * H, 0.20 * H),
        (0.60 * H, 0.35 * H),
        (0.50 * H, 0.45 * H)
    ]

    # 将这些位置转换为当前坐标系（以中心为原点）
    small_centers = []
    for dx, dy in small_positions_H_units:
        sx = -W/2 + dx
        sy = H/2 - dy
        small_centers.append((sx, sy))

    # 绘制四颗小星：每颗星的一尖朝向大星中心
    for (sx, sy) in small_centers:
        # 计算从小星中心指向大星中心的角度
        ang_rad = math.atan2(big_cy - sy, big_cx - sx)   # 返回弧度
        ang_deg = math.degrees(ang_rad)
        # 第一个外顶点（pts[0]）朝向大星中心
        rotation_for_small = ang_deg
        draw_star_polygon(sx, sy, small_r, rotation_for_small, star_yellow)

    hideturtle()
    done()

if __name__ == "__main__":
    draw_china_flag()