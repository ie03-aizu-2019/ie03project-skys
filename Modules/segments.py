"""
クラス
- segment: 線分
- point: 点

関数
- find_intersection(): 2線分の交点を求める, [交点の有無, (有れば)交点]
- find_all_intersections():
"""


class segment:  # 線分クラス
    def __init__(self, s):  # 線分はpointオブジェクトのリストで渡す
        self.P = s[0]
        self.Q = s[1]
        self.contacted = [self.P, self.Q]
        self.P.set_contacted(self)
        self.Q.set_contacted(self)

    def to_str(self):  # 線分を構成する点P, Qの座標を返す
        info = f"P = ({self.P.x}, {self.Q.y})\n"
        info = info + f"Q = ({self.Q.x}, {self.Q.y})"
        return info

    def set_contacted(self, point):
        # 接点のリストを追加
        self.contacted.append(point)

    def set_index(self, index):
        self.index = index

    def isPoint(self):
        return False


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
            returnset[1].set_contacted(s1)
            returnset[1].set_contacted(s2)
            s1.set_contacted(returnset[1])
            s2.set_contacted(returnset[1])

        else:
            # 交差なし
            pass

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
                            intersections.append(tmp[1])
                            break
                        else:
                            # 次のループへ
                            continue
    return intersections
