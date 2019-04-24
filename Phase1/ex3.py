# # コメントアウトしといて
# import sys
# sys.path.append("/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/")
import ex1
import ex2


class Manager:
    points = {}  # 資料に合わせてindex=1から振りたいのでディクショナリ
    segments = {}  # 資料に合わせてindex=1から振りたいのでディクショナリ
    intersections = {}  # 資料に合わせてindex=C1から振りたいのでディクショナリ
    roots = {}
    """
    roots[始点インデックス] = {
        終点インデックス: [経由点情報, 距離],
    }
    """

    def __init__(self):
        self.input()

    def input(self, file=False):
        M, M, P, Q, points, segments, roots = False

        if file:
            # ファイルから入力を得る
            M, M, P, Q, points, segments, roots = ex1.input_info()
        else:
            # キーボードから入力を得る
            M, M, P, Q, points, segments, roots = ex2.input_from_file()

        self.points = list2dict(points)
        self.segments = list2dict(segments)

        self.find_all_intersection()

        # root についてはあとで追記する

    def find_all_intersections(self):
        intersections = []
        segments = list(self.segments.values())
        for i in range(self.M):
            for j in range(i, self.M):
                tmp = ex1.find_intersection(segments[i], segments[j])
                if tmp[0]:  # 交点あり
                    # print(f"check A, {tmp[1].to_str()}")
                    segments[i].set_contacted(tmp[1])
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
        self.intersections = intersections
        list2dict(self.intersections)

    def search_root(self, start, fin):
        roots = []
        now = [start]

        for p in now:
            for s in p.contacted:

    def contacted(self, token, fin):
        # 再帰的に呼び出す
        next = token.contacted
        flag = False
        for t in next:
            if t is fin:
                flag = True
                break





def list2dict(l):
    length = len(l)
    d = {}
    for i in range(length):
        d[i+1] = l[i]
        # dの要素はPointまたはSegment
        d[i+1].set_index(i+1)
    return d
