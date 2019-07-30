"""
クラス
- Root: 道
- segment: 線分
- point: 点

関数
- find_intersection(): 2線分の交点を求める, [交点の有無, (有れば)交点]
- find_all_intersections(): 与線分の全ての交点を返す
- calc_shortest_connection(s, p): セグメントsと点pを接続するときの最短の接続経路を求める. return [交点, 距離]
- distance()
"""

import math
import random
import manager
from concurrent.futures import ProcessPoolExecutor


INFTY = 10**20


class Root:
    """
    - 経由点(Point型)リスト
    - 距離
    """
    # 属性--------------------
    # .points
    # .segments
    # .start
    # .fin
    # .distance
    # -------------------------
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
        info += f"\ndistance: {self.distance}"
        return info


class segment:  # 線分クラス
    # 属性---------------------
    # .P
    # .Q
    # .contacted
    # .added
    # --------------------------
    def __init__(self, s):  # 線分はpointオブジェクトのリストで渡す
        self.P = s[0]
        self.Q = s[1]
        self.contacted = [self.P, self.Q]
        self.P.set_contacted(self)
        self.Q.set_contacted(self)
        self.set_ab()
        self.set_range()
        if self.P.added or self.Q.added:
            self.added = True
        else:
            self.added = False

    def sort(self):
        # self.P, ? ? self.Q となるように.
        contacted = self.contacted
        self.contacted = []
        for i in range(len(contacted)):
            if contacted[i] is self.P or contacted[i] is self.Q:
                continue
            else:
                flag = False
                for j in range(len(self.contacted)):
                    dis1 = distance(contacted[i], self.P)
                    dis2 = distance(self.contacted[j], self.P)
                    if dis1 < dis2:
                        self.contacted.insert(j, contacted[j])
                        flag = True
                        break
                if not flag:
                    self.contacted.append(contacted[i])
        self.contacted.append(self.Q)
        self.contacted.insert(0, self.P)

    def to_str(self):  # 線分を構成する点P, Qの座標を返す
        info = f"P = ({self.P.x}, {self.P.y})\n"
        info = info + f"Q = ({self.Q.x}, {self.Q.y})"
        return info

    def set_contacted(self, point):
        # 接点のリストを追加
        # 中途で交点がみつかったときのみ使用

        min = 0
        max = len(self.contacted)-1
        mid = max // 2
        dis1 = distance(self.P, point)  # 新しい点との距離

        while(True):
            dis2 = distance(self.P, self.contacted[mid])
            if min == max:
                if dis2 < dis1:
                    mid += 1
                elif dis1 == dis2:
                    break
                    # 格納済み
                self.contacted.insert(mid, point)
                break
            # 次ループ用
            if dis1 > dis2:
                min = mid + 1
                mid = min + (max-min) // 2
            elif dis1 == dis2:
                break
            else:  # tmp[1].x < intersections[mid].
                max = mid
                mid = min + (max-min) // 2

        # for i in range(1, len(self.contacted)):
        #     dis2 = distance(self.P, self.contacted[mid])
        #     if dis2 < dis1:
        #         self.contacted.insert(i, point)
        #         break

        # ループを抜けても格納できていない -> self.Q = point

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
        if y is None:
            return False
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
        try:
            self.a = (self.P.y - self.Q.y) / (self.P.x - self.Q.x)
            self.b = self.P.y - self.a * self.P.x
        except Exception:  # Zero Devison
            self.a = None
            self.b = None

    def f(self, x):
        """
        y = f(x)を返す
        [y, True/False]
        """
        if self.a == 0:
            y = self.P.y
        elif self.a is None:
            y = None
        else:
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
        self.added = False
        self.intersect = False

    def to_str(self):
        return f"({self.x}, {self.y})"

    def equal(self, p):
        if self.x == p.x and self.y == p.y:
            return True
        else:
            return False

    def set_contacted(self, segment):
        # 接線リスト
        if segment in self.contacted:
            # 既に格納済み
            return False
        self.contacted.append(segment)

    def set_index(self, index):
        # Managerクラスより実行
        self.index = index

    def isPoint(self):
        return True

    def setAddedTrue(self):
        self.added = True

    def setIntersectTrue(self):
        self.intersect = True


def find_intersection_multi(args):
    return find_intersection(args[0], args[1])


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
            returnset[1].setIntersectTrue()

        else:
            # 交差なし
            return returnset

    is_end = False
    segs = [s1, s2]
    for i in range(2):
        for p in [segs[i].P, segs[i].Q]:
            if returnset[1].equal(p):  # 端点である
                is_end = True
                p.set_contacted(segs[(i+1) % 2])
                p.setIntersectTrue()
                segs[(i+1) % 2].set_contacted(p)

    if is_end:
        return [False]

    returnset[1].set_contacted(s1)
    s1.set_contacted(returnset[1])
    returnset[1].set_contacted(s2)
    s2.set_contacted(returnset[1])

    # [True, 交点]
    # [False]
    return returnset


def find_all_intersections(M, segments, multi=False):
    intersections = []
    if multi:
        args = []
        for i in range(M):
            for j in range(i+1, M):
                args.append((segments[i], segments[j]))

        with ProcessPoolExecutor() as executor:
            results = executor.map(find_intersection_multi, args)

        for result in results:
            if result[0]:
                intersections.append(result[1])
    else:
        for i in range(M):
            for j in range(i+1, M):
                if manager.debug:
                    manager.debugs['intersections'] = f"{i}/{M}"
                    debug_print(manager.debugs)
                result = find_intersection(segments[i], segments[j])
                if result[0]:
                    intersections.append(result[1])

    intersections = sort_points(intersections)
    return intersections


def calc_shortest_connection(s, p):
    """
    1線分と1点を引数に, 最も短い距離で接続する場合の交点と距離を返す関数
    垂直に交わると仮定したときの交点x, yを求める
    1. セグメントの傾き=0のとき
        y = s.P.y
        x = p.x
    2. セグメントの傾き=∞(None)のとき, x=定数
        y = p.y
        x = s.P.x
    3. y = ax + b で表されるとき
        方程式を解く
    """

    if s.a == 0:
        x = p.x
        y = [s.P.y, (s.P.x <= p.x and s.Q.x >= p.x
                     or s.Q.x <= p.x and s.P.x >= p.x)]
    elif s.a is None:
        x = s.P.x
        y = [p.y, (s.P.y <= p.y and s.Q.y >= p.y
                   or s.Q.y <= p.y and s.P.y >= p.y)]
    else:
        a = -1 / s.a
        b = p.y - a * p.x
        x = (b - s.b) / (s.a - a)
        y = s.f(x)

    if y[1]:  # 垂直に交わる
        intersection = [point([x, y[0]])]
        intersection.append(distance(intersection[0], p))
    else:  # 垂直に交わらない
        dis1 = distance(s.P, p)
        dis2 = distance(s.Q, p)

        if dis1 < dis2:  # Pと繋ぐのが最短
            intersection = [point([s.P.x, s.P.y]), dis1]
        else:
            intersection = [point([s.Q.x, s.Q.y]), dis2]

    return intersection  # [交点, 距離]


def debug_print(debugs):
    message = f"find_intersects: {debugs['intersections']}"
    print(f"\r{message}", end="")


def isBigger(p1, p2):  # p1 >= p2ならTrue
    if p1.x > p2.x:
        return True
    elif p1.x == p2.x:
        if p1.y >= p2.y:
            return True
        else:
            return False
    else:
        return False


def sort_points(data):
    if len(data) == 0:
        return data
    elif len(data) == 1:
        return data
    elif len(data) == 2:
        if isBigger(data[0], data[1]):
            return [data[1], data[0]]
        else:
            return [data[0], data[1]]
    flag = False
    i = 0
    j = len(data)-1
    rands = []
    for k in range(3):
        try:
            rand = random.randint(i, j)
        except Exception:
            print(f"i: {i}")
            print(f"j: {j}")
        index = k
        for l in range(k):
            if data[rand].x < data[rands[l]].x:
                index = l
                break
            else:
                continue
        rands.insert(index, rand)
    axis = rands[1]
    axis_value = data[axis]
    while(True):
        if flag:  # 終了
            break
        while(True):
            if i == j:
                flag = True
                break
            elif isBigger(data[i], axis_value):
                break
            i += 1
        while(True):
            if flag:
                j += 1
                break
            elif i == j:
                flag = True
                break
            elif not isBigger(data[j], axis_value):
                break
            j -= 1
        if not flag:
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp

    first = data[0:j]
    second = data[j:len(data)]
    if first == []:
        return data
    first = sort_points(first)
    second = sort_points(second)
    first.extend(second)
    return first


def distance(in1, in2):
    # 越川編集
    if in1 is None or in2 is None:  # 到達不可 -> 距離∞
        return INFTY
    return math.sqrt(
        (in2.x - in1.x)*(in2.x - in1.x) + (in2.y - in1.y)*(in2.y - in1.y)
        )


def calc_cos(vec1, vec2):
    x1 = vec1[0]
    y1 = vec1[1]
    x2 = vec2[0]
    y2 = vec2[1]
    length_a = math.sqrt(x1**2 + y1**2)
    length_b = math.sqrt(x2**2 + y2**2)
    return (x1*x2 + y1*y2) / (length_a * length_b)


def to_vector(p1, p2):
    x_vec = p2.x - p1.x
    y_vec = p2.y - p1.y
    return (x_vec, y_vec)
