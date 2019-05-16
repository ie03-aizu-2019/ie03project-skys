# コメントアウトしといて
import sys,math
sys.path.append("/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/")
import ex1
import ex2


class Root:
    """
    - 経由点(Point型)リスト
    - 距離
    """

    def __init__(self, points_and_segments):
        self.points = []
        self.segments = []
        for token in points_and_segments:
            if token.isPoint():
                self.points.append(token)
            else:
                self.segments.append(token)
        self.start = self.points[0]
        self.fin = self.points[len(self.points)-1]
        self.distance()

    def distance(self):
        self.distance = 0
        for i in range(len(self.points)-1):
            self.distance += distance(self.points[i], self.points[i+1])

    def is_equal(self, root):
        """
        等しいと判断される条件
        - 始点, 終点が同じ
        - 同じ線分で繋がれている
        """
        flag = False
        if self.start is root.start:
            if self.fin is root.fin:
                if set(self.segments) == set(root.segments):
                    flag = True
        return flag

    def to_str(self):
        print("Points: ", end="")
        for point in self.points:
            print(f"{point.index}", end=" ")
        print("\nSegments: ", end="")
        for segment in self.segments:
            print(f"{segment.index}", end=" ")
        print(f"\ndistance: {self.distance}")


class Manager:
    """
    roots[始点インデックス] = {
        終点インデックス: [経由点情報, 距離],
    }
    """

    def __init__(self):
        pass
        self.points = {}  # 資料に合わせてindex=1から振りたいのでディクショナリ
        self.segments = {}  # 資料に合わせてindex=1から振りたいのでディクショナリ
        self.intersections = {}  # 資料に合わせてindex=C1から振りたいのでディクショナリ
        self.roots = {}

    def input(self, file=False, path="/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/input.txt"):
        N, M, P, Q, points, segments, roots = range(7)

        if file:
            # ファイルから入力を得る
            self.N, self.M, self.P, self.Q, points, segments, roots = ex2.input_from_file(
                path=path)
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
        roots = self.searching(start, fin, vias=[], roots=[])
        sorted = []
        if len(roots) == 0:  # ルートなし
            self.roots[start.index] = {
                fin.index: [None]
                }
        else:  # ルートあり → ルートを近い順にソート
            sorted.append(Root(roots[0]))
            for i in range(1, len(roots)):
                root = Root(roots[i])
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
        # start, finはポイントクラスオブジェクト
        # 再帰的に呼び出す
        # return 経由点

        # print(vias)
        # print(roots)

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
    # 越川編集
    return math.sqrt((in2.x - in1.x)*(in2.x - in1.x) + (in2.y - in1.y)*(in2.y - in1.y))


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
            if res is None:  # 道無し
                print("NA")
            else:
                print(res.distance)
        else:
            print("NA")
