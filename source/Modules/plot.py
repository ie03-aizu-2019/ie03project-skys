"""
図をプロットする系

関数
- plot_all()
"""

# import os
import numpy as np
# numpyモジュールをnpとして使える
import matplotlib.pyplot as plt
# matplotlib.pyplotモジュールをpltとして使える
import path

figsize = (8, 5.25)


def plot_all(points={}, segments={}, delta=0.01, save=False, path=path.figure_path):
    # segments -> intersections -> point の順にプロットする
    plt.figure(figsize=figsize)
    s_flag = False
    for index in segments:
        x1 = segments[index].P.x
        x2 = segments[index].Q.x
        y1 = segments[index].P.y
        y2 = segments[index].Q.y
        if x1 < x2:
            x_list = np.arange(x1, x2, delta)
            y_list = x_list * segments[index].a + segments[index].b
        elif x1 == x2:
            if y1 < y2:
                y_list = np.arange(y1, y2, delta)
                x_list = y_list * 0 + x1
            else:
                y_list = np.arange(y2, y1, delta)
                x_list = y_list * 0 + x1
        else:
            x_list = np.arange(x2, x1, delta)
            y_list = x_list * segments[index].a + segments[index].b
        label = ""
        if not s_flag:
            label = "Segment"
            s_flag = True
        plt.plot(x_list, y_list, color="blue", ls="-", label=label)

    p_flag = False
    i_flag = False
    # 以下のプロウラムで図のレイアウトを決定
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
