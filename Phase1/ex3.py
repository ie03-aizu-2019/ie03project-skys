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

    def output(self):


    def find_all_intersections(self):
        intersections = []
        segments = list(self.segments.values())
        for i in range(self.M):
            for j in range(i, self.M):
                tmp = ex1.find_intersection(segments[i], segments[j])
                if tmp[0]:  # 交点あり
                    # Segmentに接点情報を追加
                    # segments[i].set_contacted(tmp[1])
                    # segments[j].set_contacted(tmp[1])
                    # tmp[1].set_contacted(segments)
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
        list2dict(self.intersections, intersections=True)

    def search_root(self, start, fin):
        # start, finはポイントクラスオブジェクト
        roots = self.searching(start, fin)
        mins = []
        mins.append(roots[0])
        for i in range(1, len(roots)):
            if mins[0][1] == roots[i][1]:
                # 最短ルート追加
                mins.append(roots[i][1])
            elif mins[0][1] > roots[i][1]:
                 # 最短ルート更新
                 mins = []
                 mins.append(roots[i])

        if len(mins) == 0:
            self.roots[start.index][fin.index] = [
                ["NA", "NA"]
            ]
        else:
            self.roots[start.index][fin.index] = [
                [mins[0]]
                # mins[0] = [経由点リスト, 距離]
            ]

    def searching(self, start, fin, vias=[], roots=[]):
        # start, finはポイントクラスオブジェクト
        # 再帰的に呼び出す
        # return 経由点

        success = False
        end = False
        if start.isPoint():
            vias.append(start)

        if start is fin:
            success = True

        for via in vias:
            if start is via:
                end = True
                break

        if success:
            dis = 0
            for i in range(len(vias)-1):
                dis += distance(vias[i], vias[i+1])
            roots.append([vias, dis])

        elif end:
            pass

        else:  # return条件を満たさなければ, 以下再帰へ.
            tmp = []
            for t in start.contacted:
                result = self.search_root(t, fin, vias=vias, roots=roots)

                # rootsのmerge
                for r_info in result:
                    flag = False
                    for r_info2 in tmp:
                        if r_info is r_info2:
                            flag = True
                    if flag:
                        roots.append(r_info)

        return roots


def list2dict(l, intersections=False):
    length = len(l)
    d = {}
    for i in range(length):
        if intersections:
            d[f"C{i+1}"] = l[i]
            # dの要素はPointまたはSegment
            d[f"C{i+1}"].set_index(f"C{i+1}")
        else:
            d[f"{i+1}"] = l[i]
            # dの要素はPointまたはSegment
            d[f"{i+1}"].set_index(f"{i+1}")
    return d
