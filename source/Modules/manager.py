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
    def __init__(self):
        self.points = {}  # index=1からN
        self.segments = {}  # index=1からM
        self.roots_index = []  # 探索するルートの添字
        self.added_points = []
        self.roots = {}  # 探索したルートの結果

    def input(self, file=True, path=None):
        self.input2(file, path)
        self.find_all_intersections()

    def input2(self, file=False, path=None):
        N, M, P, Q, points, segments, roots = range(7)

        if file:
            # ファイルから入力を得る
            if path is None:  # 標準パス
                self.N, self.M, self.P, self.Q, points, segments, added_points, roots_index = input.input_from_file()
            else:  # パスの入力あり
                self.N, self.M, self.P, self.Q, points, segments, added_points, roots_index = input.input_from_file(
                    path=path)
        else:
            # キーボードから入力を得る
            self.N, self.M, self.P, self.Q, points, segments, added_points, roots_index = input.input_from_stdin()
        self.points = list2dict(points)
        self.segments = list2dict(segments)
        self.added_points = added_points
        self.roots_index = roots_index

    def run(self, ex):
        if type(ex) is not int:
            try:
                ex = int(ex)
            except Exception as e:
                print(e)
                return False

        if ex == 1:
            self.ex1()
        elif ex == 2:
            self.ex2()
        elif ex == 3:
            self.ex3()
        elif ex == 4:
            self.ex4()
        elif ex == 5:
            self.ex5()
        elif ex == 6:
            self.ex6()
        elif ex == 7:
            self.ex7()
        # elif ex == 8:
            # self.ex8()
        else:
            return False

        return True

    def print_info(self, length=3):
        print(f"N(Number of Points)\t\t: {self.N}")
        print(f"M(Number of Segments)\t\t: {self.M}")
        print(f"P(Number of adding Points)\t: {self.P}")
        print(f"Q(Number of Roots)\t\t: {self.Q}")

        print("-- Points --")
        for key in list(self.points):
            if not self.points[key].added:
                print(f"{key}: {self.points[key].to_str()}")

        print("-- Segments --")
        for key in list(self.segments):
            P = self.segments[key].P
            Q = self.segments[key].Q
            print(f"{key}: {P.index}({P.x}, {P.y}) -> {Q.index}({Q.x}, {Q.y})")

        print("-- Added Points --")
        for key in list(self.points):
            if self.points[key].added and "C" not in key:
                print(f"{key}: {self.points[key].to_str()}")

        for key in list(self.points):
            if self.points[key].added and "C" in key:
                print(f"{key}: {self.points[key].to_str()}")

        print("-- Roots --")
        for index in self.roots_index:
            print(f"  # From {index[0]} To {index[1]}")
            try:
                tmp = self.roots[index[0]][index[1]]
            except Exception:
                tmp = None

            if tmp is not None:
                for i in range(length):
                    try:
                        if tmp[i] is not None:
                            print(tmp[i].to_str(), end="\n\n")
                    except Exception:  # length out of range
                        pass

    def plot(self, save=False, path=None):
        plot.plot_all(self.points, self.segments, save=save, path=path)

    def find_all_intersections(self):
        segments = list(self.segments.values())
        intersections = sg.find_all_intersections(self.M, segments)
        intersections = list2dict(intersections, intersections=True)
        for index in list(intersections):
            self.points[index] = intersections[index]

    def search_all_root(self):
        for root in self.roots_index:
            try:
                self.search_root(self.points[root[0]], self.points[root[1]])
            except Exception as e:
                # KeyError
                print(e)

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
            # self.roots[start.index][fin.index] = [
            #     root1,
            #     root2,
            # ]

    def searching(self, start, fin, vias=[], roots=[]):
        """
        start, finはポイントクラスオブジェクト
        再帰的に呼び出す
        return 経由点
        """

        success = False
        end = False

        # for via in vias:
        #     if via.isPoint() and start is via:
        #         end = True
        #         break

        if start in vias:
            end = True

        vias.append(start)

        if start is fin:
            success = True

        if success:
            # 再帰の末尾
            roots.append(vias)
        elif end:
            pass
        else:  # 条件を満たさなければ, 以下再帰へ
            # 線分用再帰⇓
            if (not start.isPoint()) and len(start.contacted) >= 3:
                bef = vias[len(vias)-2]
                plus = None
                minus = None
                flag = False

                for p in start.contacted:
                    if flag:
                        plus = p
                        break
                    elif p is not bef:
                        minus = p
                        continue
                    else:
                        flag = True

                if plus is not None:
                    self.searching(plus, fin, vias=[
                                   x for x in vias], roots=roots)
                if minus is not None:
                    if minus not in vias:
                        self.searching(minus, fin, vias=[
                                       x for x in vias], roots=roots)
            else:
                for t in start.contacted:
                    self.searching(t, fin, vias=[x for x in vias], roots=roots)

        return roots

    def next_index(self):
        max = -1
        indexs = {}
        for i in list(self.segments):
            if max < int(i):
                max = int(i)
        indexs['segment'] = str(max+1)
        max = -1
        max_2 = -1
        for i in list(self.points):
            if "C" in i:
                if max < int(i.replace("C", "")):
                    max = int(i.replace("C", ""))
            else:
                if max_2 < int(i):
                    max_2 = int(i)
        indexs['point'] = str(max_2+1)
        indexs['intersection'] = "C" + str(max+1)
        return indexs

    def add_point(self, p):
        # もっとも短い繋ぎ方で道路に繋ぐ
        # [交点, 距離]
        min_set = sg.calc_shortest_connection(self.segments['1'], p)
        connected_seg = self.segments['1']

        for key in list(self.segments)[1:]:
            result = sg.calc_shortest_connection(self.segments[key], p)
            if result[1] < min_set[1]:
                connected_seg = self.segments[key]
                min_set = result

        # 追加
        min_set[0].setAddedTrue()
        p.setAddedTrue()
        seg = sg.segment([min_set[0], p])  # 追加点と交点を結ぶ線分
        # 線分, 点の追加
        indexs = self.next_index()
        p.set_index(indexs['point'])
        min_set[0].set_index(indexs['intersection'])
        self.segments[indexs['segment']] = seg
        self.points[indexs['point']] = p
        if min_set[0].equal(connected_seg.P) or min_set[0].equal(connected_seg.Q):
            # 端点である(=intersectionsに含めない)
            indexs = self.next_index()
            self.points[indexs['point']] = min_set[0]
        else:
            self.points[indexs['intersection']] = min_set[0]

    def add_all_points(self):
        for p in self.added_points:
            self.add_point(p)
        self.added_points = []

    # ⇓各課題の出力メソッド⇓
    def ex1(self):
        ans = sg.find_intersection(self.segments['1'], self.segments['2'])
        if not ans[0]:  # 交点なし
            print("NA")
        else:  # 交点あり
            print(f"{ans[1].x:.5f} {ans[1].y:.5f}")

    def ex2(self):
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

    def ex5(self):
        self.search_all_root()
        for index in self.roots_index:
            start = index[0]
            fin = index[1]
            roots = self.roots[start][fin]
            K = int(index[2])
            if len(roots) < K:
                K = len(roots)
            for i in range(K):
                print(f"{roots[i].distance:.5f}")

    def ex6(self):
        self.search_all_root()
        for index in self.roots_index:
            start = index[0]
            fin = index[1]
            roots = self.roots[start][fin]
            K = int(index[2])
            if len(roots) < K:
                K = len(roots)
            for i in range(K):
                print(f"{roots[i].distance:.5f}")
                # root.points = [point(1), point(C1), point(4)]
                for point in roots[i].points:
                    print(point.index, end=", ")
                print()

    def ex7(self):
        self.add_all_points()
        for p in self.points:
            if self.points[p].added and (self.points[p] not in self.added_points):
                if len(str(self.points[p].x)) >= 7:
                    print(f"{self.points[p].x:.5f}", end=" ")
                else:
                    print(self.points[p].x, end=" ")
                if len(str(self.points[p].y)) >= 7:
                    print(f"{self.points[p].y:.5f}")
                else:
                    print(self.points[p].y)


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
