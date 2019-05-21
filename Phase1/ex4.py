"""
小課題4
小課題3の仮定で経路も求めているのでそれを出力するようにする

また, 小課題1-4に対応する出力メソッドをManagerに用意する
"""

import sys
# sys.path.append("/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/")
sys.path.append(
    "/Users/koshikawasora/Desktop/synthesis/ie03project-skys/Phase1")
import ex3
import ex1


class Manager4(ex3.Manager):
    def ex1(self):
        ans = ex1.find_intersection(self.segments['1'], self.segments['2'])
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
                    print(f"{res.distance:.5f}")
                    for point in res.points:
                        print(point.index, end=" ")
                    print()
            else:
                print("NA")


# if __name__ == "__main__":
#     M = Manager4()
#     # M.input()
#     M.input(file=True)
#     M.ex4()

M = Manager4()
M.input(file=True, path="/Users/koshikawasora/Desktop/synthesis/ie03project-skys/Phase1/input.txt")
M.ex4()
