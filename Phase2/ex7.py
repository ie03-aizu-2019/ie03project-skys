"""
座標から, 傾きと切片を求める
a = (y1 - y2) / (x1 - x2)
b = y1 - a * x1

a2(新しい道候補) = -1 / a
"""

import Phase1.ex1 as ex1
import Phase1.ex3 as ex3

p1 = ex1.point([2, 5])
p2 = ex1.point([7, 1])
s1 = ex1.segment([p1, p2])
s1.set_ab()


q1 = ex1.point([5, 1])


def calc_shortest_connection(s, p):
    """
    1線分と1点を引数に, 最も短い距離で接続する場合の交点と距離を返す関数
    """
    a = -1 / s.a
    b = p.y - a * p.x

    x = (b - s.b) / (s.a - a)
    y = s.f(x)

    if not y[1]:  # 垂直に交わる
        intersection = [ex1.point([x, y])]
        intersection.append(ex3.distance(intersection[0], p))
    else:  # 垂直に交わらない
        p = ex1.point([x, y[0]])

        dis1 = ex3.distance(s.P, p)
        dis2 = ex3.distance(s.Q, p)

        if dis1 < dis2:  # Pと繋ぐのが最短
            intersection = [ex1.point([s.P.x, s.P.y]), dis1]
        else:
            intersection = [ex1.point([s.Q.x, s.Q.y]), dis2]

    return intersection  # [交点, 距離]


"""
追加地点Q -> pointインスタンス(q)生成
全てのセグメント(s)に対して,
result <- 追加: calc_shortest_connection(s, q)
resultの中でもっとも短いものを答えとする
"""

res = calc_shortest_connection(s1, q1)

res[0].to_str()
