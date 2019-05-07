# コメントアウトしといて
import sys
sys.path.append("/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/")
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
        pass

    def input(self, file=False, path="/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/input.txt"):
        N, M, P, Q, points, segments, roots = range(7)

        if file:
            # ファイルから入力を得る
            self.N, self.M, self.P, self.Q, points, segments, roots = ex2.input_from_file(path=path)
        else:
            # キーボードから入力を得る
            self.N, self.M, self.P, self.Q, points, segments, roots = ex1.input_info()
        self.points = list2dict(points)
        self.segments = list2dict(segments)

        self.find_all_intersections()
        self.roots_index = roots


    def print_info(self):
        print(f"N: {self.N}")
        print(f"M: {self.M}")
        print(f"P: {self.P}")
        print(f"Q: {self.Q}")
        print("-- Points --")
        for key in list(self.points):
            print(f"{key}: {self.points[key].to_str()}")
        print("-- Segments --")
        for key in list(self.segments):
            print(f"{key}: {self.segments[key].to_str()}")
        print("-- Roots_index --")
        print(self.roots_index)

    def find_all_intersections(self):
        segments = list(self.segments.values())
        intersections = ex2.find_all_intersections(self.M, segments)
        intersections = list2dict(intersections, intersections=True)
        for index in list(intersections):
            self.points[index] = intersections[index]

    def search_root(self, start, fin):
        # start, finはポイントクラスオブジェクト
        # 再帰的に全てのルートと距離を取得
        roots = self.searching(start, fin)
        sorted = []
        if len(roots) == 0:  # ルートなし
            self.roots[start.index] = {
                fin.index: [[None, None]]
                }
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
            if not start.index in self.roots.keys():
                self.roots[start.index] = {}
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

        for via in vias:
            if start is via:
                end = True
                break

        if start.isPoint():
            vias.append(start)

        if start is fin:
            success = True

        if success:
            # 再帰の末尾
            # print("Success!!")
            # print(f"Start:{start.to_str()}, End: {fin.to_str()}")
            dis = 0
            for i in range(len(vias)-1):
                dis += distance(vias[i], vias[i+1])
            #     print(vias[i].to_str(), end=" -> ")
            # print(vias[len(vias)-1].to_str())
            roots.append([vias, dis])
        elif end:
            pass
        else:  # 条件を満たさなければ, 以下再帰へ
            vias_copy = []
            for t in start.contacted:
                result = self.searching(t, fin, vias=[x for x in vias], roots=roots)
                # rootsの結合
                # for r1 in result:
                #     flag = False
                #     for r2 in roots:
                #         if r1 is r2:
                #             flag = True
                #     if not flag:
                #         roots.append(r1)

        return roots


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


def distance(in1, in2):
    # 仮
    return 10


# デバッグ
if __name__ == "__main__":
    M = Manager()
    M.input(file=True)
    for root in M.roots_index:
        # root = ["開始", "終了", "順位"]
        success_flag = True
        try:
            M.search_root(M.points[root[0]], M.points[root[1]])
        except Exception:
            # KeyError
            success_flag = False
        if success_flag:
            res = M.roots[root[0]][root[1]]
            # 順位(入力) - 1 = 順位に対応する経路の添字
            res = res[int(root[2])-1]
            # res = [経由点リスト, 距離]
            if res[0][0] is None:  # 道無し
                print("NA")
            else:
                print(res[1])
        else:
            print("NA")
