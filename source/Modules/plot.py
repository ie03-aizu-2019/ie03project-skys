"""
図をプロットする系

関数
- plot_all()
"""

# import os
import numpy as np
import matplotlib.pyplot as plt
import path

figsize = (8, 5.25)


def plot_all(points={}, segments={}, delta=0.01, save=False, path=path.figure_path):
    # segments -> intersections -> point の順にプロットする
    plt.figure(figsize=figsize)
    s_flag = False
    for index in segments:
        x1 = segments[index].P.x
        x2 = segments[index].Q.x
        if x1 < x2:
            x_list = np.arange(x1, x2, delta)
        else:
            x_list = np.arange(x2, x1, delta)
        label = ""
        if not s_flag:
            label = "Segment"
            s_flag = True
        plt.plot(x_list, x_list * segments[index].a
                 + segments[index].b, color="blue", ls="-", label=label)

    p_flag = False
    i_flag = False
    for index in points:
        color = "red"
        label = ""
        if "C" in index:
            color = "magenta"
            if not i_flag:
                label = "Intersection"
                i_flag = True
        else:
            if not p_flag:
                label = "Point"
                p_flag = True
        plt.plot(points[index].x, points[index].y,
                 color=color, marker="*", label=label)

    # その他の設定
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Points, Segments, Intersections")
    plt.legend()
    if save:  # 保存
        plt.savefig('../static/figure.png')
    else:  # or 表示
        plt.show()
