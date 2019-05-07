"""
クラス
- Manager

関数
- list2dict()
"""


import segments as sg
import input


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
        pass

    def input(self, file=False):
        M, M, P, Q, points, segments, roots = False

        if file:
            # ファイルから入力を得る
            M, M, P, Q, points, segments, roots = input.input_from_stdin()
        else:
            # キーボードから入力を得る
            M, M, P, Q, points, segments, roots = input.input_from_file()

        self.points = list2dict(points)
        self.segments = list2dict(segments)

        self.find_all_intersection()
        self.roots_index = roots

    def find_all_intersections(self):
        segments = list(self.segments.values())
        intersections = sg.find_all_intersections(self.M, segments)
        intersections = list2dict(intersections, intersections=True)
        for index in list(intersections):
            self.points[index] = intersections[index]

    def search_root(self, start, fin):
        # start, finはポイントクラスオブジェクト
        # 再帰的に全てのルートと距離を取得
        roots = self.searching(start, fin)
        sorted = []
        if len(roots) == 0:  # ルートなし
            self.roots[start.index][fin.index] = [
                ["NA", "NA"]
            ]
        else:  # ルートあり → ルートを近い順にソート
            sorted.append(roots[0])
            for i in range(1, len(roots)):
                for j in range(len(sorted)):
                    if sorted[j][1] >= roots[i][1]:
                        # ルートの追加
                        sorted.insert(j, roots[i])
                        break
                    else:
                        if j == len(sorted)-1:  # 最長ルート
                            sorted.append(roots[i])
            self.roots[start.index][fin.index] = sorted
            # sorted = [
            #     [[point1, point2, ..., pointn], distance],
            #     [[point1, point2, ..., pointn], distance],
            # ]

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

                # rootsの結合
                for r_info in result:
                    flag = False
                    for r_info2 in tmp:
                        if r_info is r_info2:
                            flag = True
                    if flag:
                        roots.append(r_info)

        return roots

    def ex1(self):
        ans = sg.find_intersection(self.segments[0], self.segments[1])
        # 交点 = 端点を除去しつつ出力する
        if not ans[0]:  # 交点なし
            print("NA")
        elif ans[1].equal(self.segments[0].P) or ans[1].equal(self.segments[0].Q) or ans[1].equal(self.segments[1].P) or ans[1].equal(self.segments[1].Q):
            # 交点ありだが端点である
            print("NA")
        else:  # 交点あり
            print(f"{ans[1].x:.5f} {ans[1].y:.5f}")

    def ex2(self):
        intersections = sg.find_all_intersections()

        for p in intersections:
            print(f"{p.x:.5f} {p.y:.5f}")

    def ex3(self):
        for root in self.roots_index:
            # root = ["開始", "終了", "順位"]
            self.search_root(self.points[root[0]], self.points[root[1]])
            # self.rootsに探索結果が格納される
            res = self.roots[root[0]][root[1]]
            # 順位(入力) - 1 = 順位に対応する経路の添字
            res = res[int(root[2])-1]
            # res = [経由点リスト, 距離]
            print(res[1])

    def ex4(self):
        for root in self.roots_index:
            # root = ["開始", "終了", "順位"]
            self.search_root(self.points[root[0]], self.points[root[1]])
            # self.rootsに探索結果が格納される
            res = self.roots[root[0]][root[1]]
            # 順位(入力) - 1 = 順位に対応する経路の添字
            res = res[int(root[2])-1]
            # res = [経由点リスト, 距離]
            print(res[1])
            for point in res[0]:  # 経由点を出力
                print(point.index, end=" ")
            print()


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
