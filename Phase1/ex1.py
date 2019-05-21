"""
小課題1 設計
1. 座標(point)クラスと線分(segment)クラスの定義
2. find_intersection(point, point) -> [True/False, point(存在するとき)]を定義
3. 入力->整数値->point->segmentへと整形
4. find_intersection(segment, segment)の戻り値を整えて出力
"""


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
        for i in range(len(self.contacted)):
            if self.contacted[i] is segment:
                # 既に格納済み
                return False
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


def input_info():
    points = []
    segments = []

    tmp = input("")  # "4 2 0 0"
    tmp = tmp.split(" ")  # ["4", "2", "0", "0"]
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i])
    # [4, 2, 0, 0]
    N, M, P, Q = tmp

    for i in range(N):  # for N回まわしてなかでinput
        tmp = input("")
        tmp = tmp.split(" ")  # "0 0" -> ["0", "0"]
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        # point([0, 0])
        points.append(point(tmp))  # points.append(point(koshikawa))

    for i in range(M):  # for m
        tmp = input()
        tmp = tmp.split(" ")
        # "0 0" ->  koshikawa = [0, 0]
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        segments.append(
            segment([points[tmp[0]-1], points[tmp[1]-1]]))
        # segments.append(segment(koshikawa))

        """
        roots [
            ["1", "4", 1],
            ["C1", "3", 1]
        ]
        """

    roots = []
    for i in range(Q):
        tmp = input("")
        tmp = tmp.split(" ")
        tmp[2] = int(tmp[2])
        # tmp = ["1", "4", 1]
        roots.append(tmp)

    for i in range(Q):
        tmp = input("")
        tmp = tmp.split(" ")
        roots[i] = tmp
        roots[i][2] = int(tmp[i][2])

    return N, M, P, Q, points, segments, roots




if __name__ == "__main__":
    N, M, P, Q, points, segments, roots = input_info()

    print(roots)

    # ans = find_intersection(segments[0], segments[1])
    #
    # if ans[0]:  # 交点あり
    #     print(f"{ans[1].x:.5f} {ans[1].y:.5f}")
    # else:
    #     print("NA")
