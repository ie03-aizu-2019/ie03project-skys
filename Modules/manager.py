"""
クラス
- Manager

メソッド
- Manager.print_info()
- Manager.input(file=False, path=None)
- Manager.exX()

関数
- list2dict()
"""

import input
import segments as sg
import plot


class Manager:
    points = {}  # index=1からN
    segments = {}  # index=1からM
    intersections = {}  # index=C1からQ
    roots_index = []  # 探索するルートの添字
    roots = {}  # 探索したルートの結果

    def __init__(self):
        pass

    def input(self, file=False, path=None):
        N, M, P, Q, points, segments, roots = range(7)

        if file:
            # ファイルから入力を得る
            if path is None:  # 標準パス
                self.N, self.M, self.P, self.Q, points, segments, roots_index = input.input_from_file()
            else:  # パスの入力あり
                self.N, self.M, self.P, self.Q, points, segments, roots_index = input.input_from_file(
                    path=path)
        else:
            # キーボードから入力を得る
            self.N, self.M, self.P, self.Q, points, segments, roots_index = input.input_from_stdin()
        self.points = list2dict(points)
        self.segments = list2dict(segments)
        self.find_all_intersections()
        self.roots_index = roots_index

    def print_info(self, detail=False):
        len = 1
        if detail:
            len = 3
        print(f"N(Number of Points)\t\t: {self.N}")
        print(f"M(Number of Segments)\t\t: {self.M}")
        print(f"P(Number of adding Points)\t: {self.P}")
        print(f"Q(Number of Roots)\t\t: {self.Q}")

        print("-- Points --")
        for key in list(self.points):
            print(f"{key}: {self.points[key].to_str()}")

        print("-- Segments --")
        for key in list(self.segments):
            P = self.segments[key].P
            Q = self.segments[key].P
            if "C" in P.index:
                print(f"{key}: {P.index}({P.x}, {P.y}) -> {Q.index}({Q.x}, {Q.y})")
            else:
                print(f"{key}: P{P.index}({P.x}, {P.y}) -> {Q.index}({Q.x}, {Q.y})")

        print("-- Roots --")
        for index in self.roots_index:
            print(f"  # From {index[0]} To {index[1]}")
            try:
                tmp = self.roots[index[0]][index[1]]
            except Exception:
                tmp = None

            if tmp is not None:
                for i in range(len):
                    if tmp[i] is not None:
                        print(tmp[i].to_str())
                        pass

    def plot(self, save=False, path=None):
        plot.plot_all(self.points, self.segments, save=save, path=path)

    def find_all_intersections(self):
        segments = list(self.segments.values())
        intersections = sg.find_all_intersections(self.M, segments)
        intersections = list2dict(intersections, intersections=True)
        for index in list(intersections):
            self.points[index] = intersections[index]

    def search_root(self, start, fin):
        # start, finはポイントクラスオブジェクト
        # 再帰的に全てのルートと距離を取得
        roots = self.searching(start, fin, vias=[], roots=[])
        sorted = []
        if len(roots) == 0:  # ルートなし
            self.roots[start.index] = {
                fin.index: [None]
                }
        else:  # ルートあり → ルートを近い順にソート
            sorted.append(sg.Root(roots[0]))
            for i in range(1, len(roots)):
                root = sg.Root(roots[i])
                for j in range(len(sorted)):
                    if root.distance < sorted[j].distance:
                        # ルートの追加
                        sorted.insert(j, root)
                        break
                    elif root.distance == sorted[j].distance:
                        if root.is_equal(sorted[j]):
                            # 同じルート
                            if len(root.points) > len(sorted[j].points):
                                # より多くの点を含むルートに置き換え
                                sorted[j] = root
                                break
                            else:
                                # そのままで追加はしない
                                break
                        else:  # 距離は等しいが, 違うルート
                            sorted.insert(j, root)
                            break
                    else:
                        if j == len(sorted)-1:  # 最長ルート
                            sorted.append(root)
            if start.index not in self.roots.keys():
                self.roots[start.index] = {}
            self.roots[start.index][fin.index] = [x for x in sorted]
            # sorted = [
            #     root1,
            #     root2,
            # ]

    def searching(self, start, fin, vias=[], roots=[]):
        """
        start, finはポイントクラスオブジェクト
        再帰的に呼び出す
        return 経由点
        """

        # print(f"searching() is called: {start.index} -> {fin.index}")

        success = False
        end = False

        for via in vias:
            if via.isPoint() and start is via:
                end = True
                break

        # if start.isPoint():
        vias.append(start)

        if start is fin:
            success = True

        if success:
            # 再帰の末尾
            roots.append(vias)
        elif end:
            pass
        else:  # 条件を満たさなければ, 以下再帰へ
            for t in start.contacted:
                self.searching(t, fin, vias=[x for x in vias], roots=roots)

        return roots

    # ⇓各課題の出力メソッド⇓
    def ex1(self):
        ans = sg.find_intersection(self.segments['1'], self.segments['2'])
        if not ans[0]:  # 交点なし
            print("NA")
        else:  # 交点あり
            print(f"{ans[1].x:.5f} {ans[1].y:.5f}")

    def ex2(self):
        self.find_all_intersections()

        for p in self.points:
            if "C" in self.points[p].index:
                print(f"{self.points[p].x:.5f} {self.points[p].y:.5f}")

    def ex3(self):
        for root in self.roots_index:
            # root = ["開始", "終了", "順位"]
            success_flag = True
            try:
                self.search_root(self.points[root[0]], self.points[root[1]])
            except Exception:
                # KeyError
                success_flag = False
            if success_flag:
                res = self.roots[root[0]][root[1]]
                # 順位(入力) - 1 = 順位に対応する経路の添字
                res = res[int(root[2])-1]
                # res = [経由点リスト, 距離]
                if res is None:  # 道無し
                    print("NA")
                else:
                    print(res.distance)
            else:
                print("NA")

    def ex4(self):
        for root in self.roots_index:
            # root = ["開始", "終了", "順位"]
            success_flag = True
            try:
                self.search_root(self.points[root[0]], self.points[root[1]])
            except Exception:
                # KeyError
                success_flag = False
            if success_flag:
                res = self.roots[root[0]][root[1]]
                # 順位(入力) - 1 = 順位に対応する経路の添字
                res = res[int(root[2])-1]
                # res = [経由点リスト, 距離]
                if res is None:  # 道無し
                    print("NA")
                else:
                    print(res.distance)
                    for point in res.points:
                        print(point.index, end=" ")
                    print()
            else:
                print("NA")


def list2dict(l, intersections=False):
    length = len(l)
    d = {}
    for i in range(length):
        if intersections:  # 交差点
            d[f"C{i+1}"] = l[i]
            d[f"C{i+1}"].set_index(f"C{i+1}")
        else:  # それ以外
            d[f"{i+1}"] = l[i]
            d[f"{i+1}"].set_index(f"{i+1}")
    return d
