# 小課題1


class segment:  # 線分クラス
    def __init__(self, s):  # 線分はpointオブジェクトのリストで渡す
        self.P = s[0]
        self.Q = s[1]

    def to_str(self):  # 線分を構成する点P, Qの座標を返す
        info = f"P = ({self.P.x}, {self.Q.y})\n"
        info = info + f"Q = ({self.Q.x}, {self.Q.y})"
        return info


class point:  # 座標クラス
    def __init__(self, p):  # 座標はリストで渡す
        self.x = p[0]
        self.y = p[1]

    def to_str(self):
        return f"({self.x}, {self.y})"

    def equal(self, p):
        if self.x == p.x and self.y == p.y:
            return True
        else:
            return False


def find_intesection(s1, s2):
    """
    線分1(s1)と線分2(s2)を渡して交点を求める関数
    s1とs2はsegmentクラス
    戻り値は [交点の有無の真偽値, x座標, y座標]
    """
    returnset = [False]
    Deter = (s1.Q.x - s1.P.x)*(s2.P.y - s2.Q.y)
    Deter += (s2.Q.x - s2.P.x)*(s1.Q.y - s1.P.y)

    if Deter == 0:
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
    if returnset[0]:
        if returnset[1].equal(s1.P) or returnset[1].equal(s1.Q) or returnset[1].equal(s2.P) or returnset[1].equal(s2.Q):
            # 交点が端点である
            returnset = [False]
    return returnset


if __name__ == "__main__":
    # テスト用
    # inputs = [
    #     [[4, 2], [0, 0]],
    #     [[0, 0], [5, 5]],
    #     [[2, 5], [7, 1]],
    #     [[1, 3], [2, 4]],
    # ]
    error_flag = False

    inputs = []
    tmp = input()  # スペース区切りで入力
    tmp = tmp.split(" ")  # リストへ変換
    for i in range(len(tmp)):
        try:
            tmp[i] = int(tmp[i])
        except Exception:
            # 入力が文字列だった場合の例外処理
            error_flag = True
            tmp[i] = 0
        if not (0 <= tmp[i] and tmp[i] <= 1000):
            error_flag = True

    for i in range(0, 13, 4):
        inputs.append([[tmp[i], tmp[i+1]], [tmp[i+2], tmp[i+3]]])

    if not (3 <= len(inputs) and len(inputs) <= 4):
        # 範囲外の値
        error_flag = True

    if not error_flag:
        segments = []  # 線分を格納するリスト
        intersected = []  # 交点を格納するリスト

        for p in inputs:  # segmentsのセット
            segments.append(segment([point(p[0]), point(p[1])]))

        for i in range(len(segments)):
            for j in range(i+1, len(segments)):
                tmp = find_intesection(segments[i], segments[j])
                if tmp[0]:
                    intersected.append(tmp[1])

        if len(intersected) == 0:
            # 交点なし
            print("NA")
        else:
            # 交点あり
            for token in intersected:
                print(f"{token.x:.5f} {token.y:.5f}")
