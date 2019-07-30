# search_root
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
# inputモジュールをインポート
import segments as sg
# segmentsモジュールをsegとして使える
import sys
import plot
# 標準ライブラリplotをインポート


dis_infty = 10000000000  # 無駄なルート探索を除去する
debug = False
debugs = {
    'searching_called': 0,
    'point_skip': 0,
    'point_general': 0,
    'intersections': ''
}


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
        # リスト型を辞書に変換
        self.segments = list2dict(segments)
        # リスト型を辞書に変換
        self.added_points = added_points
        self.roots_index = roots_index


    def run(self, ex):
        if type(ex) is not int:
            try:
                ex = int(ex)
            except Exception as e:
                print(e)
                return False
        # exの値によってどの処理をするかを決める
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
        elif ex == 8:
            self.ex8()
        elif ex == 9:
            self.ex9()
        else:
            self.ex9()

        return True

    def print_info(self, length=3):
        print(f"N(Number of Points)\t\t: {self.N}")
        print(f"M(Number of Segments)\t\t: {self.M}")
        print(f"P(Number of adding Points)\t: {self.P}")
        print(f"Q(Number of Roots)\t\t: {self.Q}")

        print("-- Points --")
        # Pointsの情報を出力
        count = 0
        for key in list(self.points):
            count += 1
            #countをlengthと同じ値になるまでインクリメント
            if count > length:
                break
            # for分を抜ける。
            if not self.points[key].added:
                print(f"{key}: {self.points[key].to_str()}", end=" ")
                print([x.index for x in self.points[key].contacted])

        print("-- Segments --")
        # Segmentsの情報を出力
        count = 0
        for key in list(self.segments):
            count += 1
            if count > length:
                break
            P = self.segments[key].P
            Q = self.segments[key].Q
            print(
                f"{key}: {P.index}({P.x}, {P.y}) -> {Q.index}({Q.x}, {Q.y})",
                end=" "
                )
            print([x.index for x in self.segments[key].contacted])

        print("-- Added Points --")
        # Added Pointsの情報を出力
        count = 0
        for key in list(self.points):
            count += 1
            if count > length:
                break
            if self.points[key].added and "C" not in key:
                print(f"{key}: {self.points[key].to_str()}")
        count = 0
        for key in list(self.points):
            count += 1
            if count > length:
                break
            if self.points[key].added and "C" in key:
                print(f"{key}: {self.points[key].to_str()}")

        print("-- Roots --")
        # Rootsの情報を出力
        count = 0
        for index in self.roots_index:
            count += 1
            if count > length:
                break
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
        # 与えられた線分から全ての交点を求める関数
        segments = list(self.segments.values())
        intersections = sg.find_all_intersections(self.M, segments)
        intersections = list2dict(intersections, intersections=True)
        # リスト型を辞書に変換。
        for index in list(intersections):
            self.points[index] = intersections[index]

    def search_all_root(self, limit=True):
        # limit = Falseにすれば全ルートを取得し, Trueなら不要な経路を除去する
        for root in self.roots_index:
            try:
                self.search_root(self.points[root[0]],
                                 self.points[root[1]],
                                 root[2],
                                 limit=limit)
            except Exception as e:
                # KeyError
                print(e)

    def search_root(self, start, fin, K, limit=True):
        # startは始点情報、finは終点情報
        # start, finはポイントクラスオブジェクト
        # 再帰的に全てのルートと距離を取得
        self.searching_index = [
            start.index,
            fin.index,
            int(K)
        ]
        # ルートが存在しない場合は, 探索をしない

        skip_flag = False
        if limit:
            if len(fin.contacted) == 0:
                skip_flag = True
            elif len(fin.contacted) == 1:
                len1 = len(fin.contacted[0].contacted[0])
                len2 = len(fin.contacted[0].contacted[1])
                if (len1 + len2) > 3:
                    print("check len=1 and isolate")
                    skip_flag = True

        if not skip_flag:
            roots = self.searching(start,
                                   fin,
                                   vias=[[], 0],
                                   roots=[],
                                   limit=limit)

        if start.index not in self.roots.keys():
            self.roots[start.index] = {}
        if len(roots) == 0:  # ルートなし
            try:
                self.roots[start.index][fin.index] = [None]
            except Exception:
                self.roots[start.index] = {
                    fin.index: [None]
                    }
        else:
            try:
                self.roots[start.index][fin.index] = [
                    sg.Root(x[0]) for x in roots
                    ]
            except Exception:
                # キーエラー
                self.roots[start.index] = {
                    fin.index: [sg.Root(x[0]) for x in roots],
                    }
            # self.roots[start.index][fin.index] = [
            #     root1,
            #     root2,
            # ]

    def get_dis_K(self, roots):
        found_num = len(roots)
        if found_num > 0:
            dis_K = roots[found_num-1][1]
        else:
            dis_K = dis_infty
        return dis_K

    def debug_print(self):
        message = f"find_intersects: {debugs['intersections']}\n"
        message = f"{message}searching: {debugs['searching_called']}, "
        message = f"{message}p_general: {debugs['point_general']}, "
        message = f"{message}p_skip: {debugs['point_skip']}, "
        start = self.searching_index[0]
        fin = self.searching_index[1]
        try:
            length = len(self.roots[start][fin])
        except Exception:
            length = 0
        message = f"{message}found: {length}"
        print(f"\r\r{message}", end="")

    def searching(self, start, fin, vias=[[], 0], roots=[], limit=True):
        """
        start, finはポイントクラスオブジェクト
        再帰的に呼び出す
        return 経由点
        """
        global debugs, debug

        if debug:
            debugs['searching_called'] += 1
            self.debug_print()

        success = False
        end = False

        if start.isPoint() and start in vias[0]:
            end = True

        vias[0].append(start)

        if start is fin:
            success = True

        if success:
            # 再帰の末尾
            pass
            if len(roots) == 0:
                roots.append(vias)
            else:
                min = 0
                max = len(roots)-1
                mid = max // 2
                while(True):
                    if min == max:
                        if roots[mid][1] < vias[1]:
                            mid += 1
                        roots.insert(mid, vias)
                        break
                    # 次ループ用
                    if vias[1] > roots[mid][1]:
                        min = mid + 1
                        mid = min + (max-min) // 2
                    else:  # tmp[1].x <= intersections[mid].
                        max = mid
                        mid = min + (max-min) // 2
        elif end:
            pass
        else:  # 条件を満たさなければ, 以下再帰へ
            # 線分用再帰⇓
            if not start.isPoint():
                bef = vias[0][len(vias[0])-2]
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

                orders = []

                if sg.distance(plus, fin) < sg.distance(minus, fin):
                    orders = [plus, minus]
                else:
                    orders = [minus, plus]
                for point in orders:
                    if point is None:
                        continue
                    dis = sg.distance(bef, point) + vias[1]
                    if self.get_dis_K(roots=roots) < dis and limit:
                        debugs['point_skip'] += 1
                    else:
                        debugs['point_general'] += 1
                        self.searching(point,
                                       fin,
                                       vias=[[x for x in vias[0]], dis],
                                       roots=roots,
                                       limit=limit)
            else:  # 点用再帰
                goal_vec = sg.to_vector(start, fin)
                sorted = []
                values = []
                for t in start.contacted:
                    cos = -1
                    if t.P.equal(start):
                        vec = sg.to_vector(t.P, t.Q)
                        cos = sg.calc_cos(goal_vec, vec)
                    elif t.Q.equal(start):
                        vec = sg.to_vector(t.Q, t.P)
                        cos = sg.calc_cos(goal_vec, vec)
                    else:
                        vec1 = sg.to_vector(start, t.P)
                        vec2 = sg.to_vector(start, t.Q)
                        if not(vec1[0] == 0 and vec1[1] == 0):
                            cos = sg.calc_cos(goal_vec, vec1)
                        if cos < 0:
                            cos = sg.calc_cos(goal_vec, vec2)

                    if sorted == []:
                        sorted.append(t)
                        values.append(cos)
                        continue
                    min = 0
                    max = len(values)-1
                    mid = max // 2
                    while(True):
                        if min == max:
                            if values[mid] > cos:
                                mid += 1
                            sorted.insert(mid, t)
                            values.insert(mid, cos)
                            break
                        # 次ループ用
                        if cos < values[mid]:
                            min = mid + 1
                            mid = min + (max-min) // 2
                        else:
                            max = mid
                            mid = min + (max-min) // 2
                for t in sorted:
                    self.searching(t,
                                   fin,
                                   vias=[[x for x in vias[0]], vias[1]+0],
                                   roots=roots,
                                   limit=limit)
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
        # 最短距離を計算
        connected_seg = self.segments['1']

        for key in list(self.segments)[1:]:
            result = sg.calc_shortest_connection(self.segments[key], p)
            if result[1] < min_set[1]:
                connected_seg = self.segments[key]
                min_set = result

        # 追加
        min_set[0].setIntersectTrue()  # 接続するための交点
        min_set[0].setAddedTrue()  # 接続するための交点
        p.setAddedTrue()  # 道路網に接続した点
        seg = sg.segment([min_set[0], p])  # 追加点と交点を結ぶ線分
        # 線分, 点の追加
        indexs = self.next_index()
        p.set_index(indexs['point'])
        min_set[0].set_index(indexs['intersection'])
        self.segments[indexs['segment']] = seg
        self.points[indexs['point']] = p
        if min_set[0].equal(
            connected_seg.P
            ) or min_set[0].equal(
                connected_seg.Q
                ):
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
        # 2つの線分から交点を求める
        if not ans[0]:  # 交点なし
            print("NA")
        else:  # 交点あり
            print(f"{ans[1].x:.5f} {ans[1].y:.5f}")

    def ex2(self):
        for p in self.points:
            if "C" in self.points[p].index:
                # 文字列"C"が含まれていたら交点。
                print(f"{self.points[p].x:.5f} {self.points[p].y:.5f}")

    def ex3(self):
        for root in self.roots_index:
            # root = ["開始", "終了", "順位"]
            success_flag = True
            try:
                self.search_root(
                    self.points[root[0]],
                    self.points[root[1]],
                    root[2],
                    limit=True)
            except Exception:
                # KeyError
                success_flag = False
            if success_flag:
                res = self.roots[root[0]][root[1]]
                # 順位(入力) - 1 = 順位に対応する経路の添字
                res = res[0]
                if res is None:  # 道無し
                    print("NA")
                else:
                    print(f"{res.distance:.6g}")
            else:
                print("NA")

    def ex4(self):
        for root in self.roots_index:
            # root = ["開始", "終了", "順位"]
            success_flag = True
            try:
                self.search_root(self.points[root[0]],
                                 self.points[root[1]],
                                 root[2],
                                 limit=True)
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
                    print(f"{res.distance:.6g}")
                    for point in res.points:
                        print(point.index, end=" ")
                    print()
            else:
                print("NA")

    def ex5(self):
        self.search_all_root()
        # 与えられた始点と終点に対しての経路を全て求める
        for index in self.roots_index:
            start = index[0]
            # 始点
            fin = index[1]
            # 終点
            roots = self.roots[start][fin]
            # 始点と終点から求まる経路情報をrootsに格納
            K = int(index[2])
            if len(roots) < K:
                K = len(roots)
            if roots[0] is None:
                # 経路が見つからないときの処理
                print("NA")
            else:
                for i in range(K):
                    # k番目までの短い経路を昇順に出力
                    print(f"{roots[i].distance:.5f}")

    def ex6(self):
        self.search_all_root()
        # 与えられた始点と終点に対しての経路を全て求める
        for index in self.roots_index:
            start = index[0]
            # 始点
            fin = index[1]
            # 終点
            try:
                roots = self.roots[start][fin]
            except Exception:
                continue
            K = int(index[2])
            # kの値を数値型で格納
            if len(roots) < K:
                K = len(roots)
                # 経路の数がk以上あっても出力する経路をkに合わせるための処理
            if roots[0] is None:
                print("NA")
                # 経路が見つからなかったときの処理
            else:
                for i in range(K):
                    print(f"{roots[i].distance:.5f}")
                    # 経路の距離を出力
                    for point in roots[i].points:
                        print(point.index, end=" ")
                        # 経路の経由地点を出力
                    print()

    def ex7(self):
        self.add_all_points()
        for p in self.points:
            if self.points[p].added and self.points[p].intersect:
                print(f"{self.points[p].x:.6g} {self.points[p].y:.6g}")

    def ex8(self):
        segments = self.search_main_road()
        for segment in segments:
            print(f"{segment.P.index} {segment.Q.index}")
        pass

    def search_main_road(self, points=None, mainRoads=[]):
        if points is None:
            points = self.points
        startPointIndex = list(points)[0]
        startPoint = points[startPointIndex]
        remainList = []
        for p in points:
            if p == startPointIndex:
                continue
            mySegments = list(self.segments.values())
            self.search_root(startPoint, points[p], 2000, False)
            try:
                rootLength = len(self.roots[startPointIndex][p])
                if self.roots[startPointIndex][p] == [None]:
                    raise Exception
                nowSegments = [
                    self.roots[startPointIndex][p][x].segments for x in range(rootLength)
                    ]
            except Exception:
                remainList.append(points[p])
            for segments in nowSegments:
                mySegments = list(
                    set(mySegments) - (set(mySegments) - set(segments))
                    )
            if mySegments:
                for seg in mySegments:
                    if seg not in mainRoads:
                        mainRoads.append(seg)
        # remainList = list(
        #     set(list(points.values())) - set(remainList)
        # )
        # print(mainRoads)
        remainDict = {}
        for point in remainList:
            remainDict[point.index] = point
        if remainList != []:
            self.search_main_road(points=remainDict, mainRoads=mainRoads)
        return mainRoads



    def ex9(self):
        """
        統合された実行
        if P, Q == 0 -> 全交差点と幹線道路
        else
            if P != 0 -> 追加地点の座標
            if Q != 0 -> 最短経路とその距離
            ※ P != 0 and ! != 0 -> 両方

        追加点と, 経路情報を出力する時
        - 道路網に接続したあとでのルート
        - 接続前のルート
        のどちらを表示するか, 今は前者の方式を取っている
        """
        if self.P == 0 and self.Q == 0:
            print("-- intersections --")
            self.ex2()
            print("-- Main Road --")
            print("Not Implemented Yet")  # 8が完成したら入れ替える
            # self.ex8()
            pass
        else:
            if self.P != 0:
                print("-- Added Points --")
                self.ex7()
            if self.Q != 0:
                print("-- Roots --")
                self.ex6()


def list2dict(l, intersections=False):
    if l is None:
        return {}
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
