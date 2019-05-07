"""
小課題4
小課題3の仮定で経路も求めているのでそれを出力するようにする

また, 小課題1-4に対応する出力メソッドをManagerに用意する
"""

import ex1
import ex2
import ex3


class Manager4(ex3.Manager):
    def ex1(self):
        ans = ex1.find_intersection(self.segments[0], self.segments[1])
        # 交点 = 端点を除去しつつ出力する
        if not ans[0]:  # 交点なし
            print("NA")
        elif ans[1].equal(self.segments[0].P) or ans[1].equal(self.segments[0].Q) or ans[1].equal(self.segments[1].P) or ans[1].equal(self.segments[1].Q):
            # 交点ありだが端点である
            print("NA")
        else:  # 交点あり
            print(f"{ans[1].x:.5f} {ans[1].y:.5f}")

    def ex2(self):
        intersections = ex2.find_all_intersections()

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
