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
        終点インデックス: [道順情報, 距離],
    }
    """

    def __init__(self):
        pass

    def input(self, file=False):
        M, M, P, Q, points, segments = False

        if file:
            # ファイルから入力を得る
            M, M, P, Q, points, segments = ex1.input_info()
        else:
            # キーボードから入力を得る
            M, M, P, Q, points, segments = ex2.input_from_file()

    def set_intersections(self):
        intersections_list = ex2.find_all_intersections(self.M, self.segments)
        for i in range(len(intersections_list)):
            self.intersections[i+1] = intersections_list[i]
