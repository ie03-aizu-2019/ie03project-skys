"""
クラス
- Root: 道
- segment: 線分
- point: 点

関数
- find_intersection(): 2線分の交点を求める, [交点の有無, (有れば)交点]
- find_all_intersections(): 与線分の全ての交点を返す
- distance()
"""

import math


class Root:
    """
    - 経由点(Point型)リスト
    - 距離
    """

    def __init__(self, points_and_segments):
        """
        points_and_segments = [P1, S1, P2, S2, ... , PN]
        """
        self.points = []
        self.segments = []
        for token in points_and_segments:
            if token.isPoint():
                self.points.append(token)
            else:
                self.segments.append(token)
        self.start = self.points[0]
        self.fin = self.points[len(self.points)-1]
        self.distance()

    def distance(self):
        self.distance = 0
        for i in range(len(self.points)-1):
            self.distance += distance(self.points[i], self.points[i+1])

    def is_equal(self, root):
        """
        等しいと判断される条件
        - 始点, 終点が同じ
        - 同じ線分で繋がれている
        """
        flag = False
        if self.start is root.start:
            if self.fin is root.fin:
                if set(list(self.segments)) == set(list(root.segments)):
                    flag = True
        return flag

    def to_str(self):
        info = ""
        info += "Points: "
        for point in self.points:
            info += f"{point.index} "
        info += "\nSegments: "
        for segment in self.segments:
            info += f"{segment.index} "
        info += f"\ndistance: {self.distance}\n"
        return info


class segment:  # 線分クラス
    def __init__(self, s):  # 線分はpointオブジェクトのリストで渡す
        self.P = s[0]
        self.Q = s[1]
        self.contacted = [self.P, self.Q]
        self.P.set_contacted(self)
        self.Q.set_contacted(self)
        self.set_ab()
        self.set_range()

    def to_str(self):  # 線分を構成する点P, Qの座標を返す
        info = f"P = ({self.P.x}, {self.P.y})\n"
        info = info + f"Q = ({self.Q.x}, {self.Q.y})"
        return info

    def set_contacted(self, point):
        # 接点のリストを追加
        for i in range(len(self.contacted)):
            if self.contacted[i] is point:
                # 既に格納済み
                return False
        self.contacted.append(point)

    def set_range(self):
        """
        定義域と値域をsetする
        範囲変数 = [最小, 最大]
        """
        if self.P.x < self.Q.x:
            self.x_range = [self.P.x, self.Q.x]
        else:
            self.x_range = [self.Q.x, self.P.x]

        if self.P.y < self.Q.y:
            self.y_range = [self.P.y, self.Q.y]
        else:
            self.y_range = [self.Q.y, self.P.y]

    def is_fill_range_x(self, x):
        if self.x_range[0] <= x and x <= self.x_range[1]:
            return True
        else:
            return False

    def is_fill_range_y(self, y):
        if self.y_range[0] <= y and y <= self.y_range[1]:
            return True
        else:
            return False

    def set_index(self, index):
        self.index = index

    def isPoint(self):
        return False

    def set_ab(self):
        """
        傾きaと切片bをsetする
        """
        self.a = (self.P.y - self.Q.y) / (self.P.x - self.Q.x)
        self.b = self.P.y - self.a * self.P.x

    def f(self, x):
        """
        y = f(x)を返す
        [y, True/False]
        """
        y = x * self.a + self.b
        if self.is_fill_range_y(y):
            return [y, True]
        else:
            # f(x)は存在しない
            return [y, False]


class point:  # 座標クラス
    def __init__(self, p):  # 座標はリストで渡す
        self.x = p[0]
        self.y = p[1]
        self.contacted = []

    def to_str(self):
        return f"({self.x}, {self.y})"

    def equal(self, p):
        if self.x == p.x and self.y == p.y:
            return True
        else:
            return False

    def set_contacted(self, segment):
        # 接線リスト
        self.contacted.append(segment)

    def set_index(self, index):
        # Managerクラスより実行
        self.index = index

    def isPoint(self):
        return True


def find_intersection(s1, s2):
    """
    線分1(s1)と線分2(s2)を渡して交点を求める関数
    s1とs2はsegmentクラス
    戻り値は [交点の有無の真偽値, 交点(Pointクラス)]
    """
    EPS = 10 ** (-7)  # 誤差除去用
    returnset = [False]
    Deter = (s1.Q.x - s1.P.x)*(s2.P.y - s2.Q.y)
    Deter += (s2.Q.x - s2.P.x)*(s1.Q.y - s1.P.y)

    if -1 * EPS <= Deter and Deter <= EPS:
        # 交差なし
        return returnset
    else:
        # 交差あり(かも)
        A = s2.P.y - s2.Q.y
        B = s2.Q.x - s2.P.x
        C = s1.P.y - s1.Q.y
        D = s1.Q.x - s1.P.x
        E = s2.P.x - s1.P.x
        F = s2.P.y - s1.P.y
        s = (A * E + B * F) / Deter
        t = (C * E + D * F) / Deter

        if 0 <= s and s <= 1 and 0 <= t and t <= 1:
            # 交差あり
            x = s1.P.x + s * (s1.Q.x - s1.P.x)
            y = s1.P.y + s * (s1.Q.y - s1.P.y)
            returnset = [True, point([x, y])]

        else:
            # 交差なし
            pass

    # 端点の除去
    if returnset[0]:  # 交点あり(端点かは不明)
        is_intersection = True
        if returnset[1].equal(s1.P):
            is_intersection = False
            s1.P.set_contacted(s2)
        if returnset[1].equal(s1.Q):
            is_intersection = False
            s1.Q.set_contacted(s2)
        if returnset[1].equal(s2.P):
            is_intersection = False
            s2.P.set_contacted(s1)
        if returnset[1].equal(s2.Q):
            is_intersection = False
            s2.Q.set_contacted(s1)
        if is_intersection:  # 交点あり(端点ではない)
            returnset[1].set_contacted(s1)
            returnset[1].set_contacted(s2)
            s1.set_contacted(returnset[1])
            s2.set_contacted(returnset[1])
        else:
            returnset = [False]

    # [True, 交点]
    # [False]
    return returnset


def find_all_intersections(M, segments):
    intersections = []
    for i in range(M):
        for j in range(i, M):
            tmp = find_intersection(segments[i], segments[j])
            if tmp[0]:  # 交点あり
                if len(intersections) == 0:
                    intersections.append(tmp[1])
                else:
                    for k in range(len(intersections)):
                        if intersections[k].x > tmp[1].x:
                            # 追加
                            intersections.insert(k, tmp[1])
                            break
                        elif intersections[k].x == tmp[1].x:
                            # y座標を比較する
                            if intersections[k].y > tmp[1].y:
                                intersections.insert(k, tmp[1])
                                break
                            else:
                                if k == len(intersections)-1:
                                    intersections.append(tmp[1])
                                    break
                                else:
                                    continue
                        elif k == len(intersections)-1:
                            # 末尾に追加
                            intersections.append(tmp[1])
                            break
                        else:
                            # 次のループへ
                            continue
    return intersections


def calc_shortest_connection(s, p):
    """
    1線分と1点を引数に, 最も短い距離で接続する場合の交点と距離を返す関数
    """
    a = -1 / s.a
    b = p.y - a * p.x

    x = (b - s.b) / (s.a - a)
    y = s.f(x)

    if not y[1]:  # 垂直に交わる
        intersection = [point([x, y])]
        intersection.append(distance(intersection[0], p))
    else:  # 垂直に交わらない
        p = point([x, y[0]])

        dis1 = distance(s.P, p)
        dis2 = distance(s.Q, p)

        if dis1 < dis2:  # Pと繋ぐのが最短
            intersection = [point([s.P.x, s.P.y]), dis1]
        else:
            intersection = [point([s.Q.x, s.Q.y]), dis2]

    return intersection  # [交点, 距離]


def distance(in1, in2):
    # 越川編集
    return math.sqrt((in2.x - in1.x)*(in2.x - in1.x) + (in2.y - in1.y)*(in2.y - in1.y))
