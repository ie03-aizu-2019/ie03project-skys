# # コメントアウトしといて
# import sys
# sys.path.append("/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/")
import ex1

"""
小課題2 設計

# アルゴリズム
小課題1のsegmentクラスとpointクラスを引き続き利用する

入力されたsegment数Mに対して,

for i in [0, ..., M-1]:
    for j in [i+1, M-1]:
        intersections.append(find_intersection())

して全ての交差点リストを得る
実際には, append(末尾から追加)ではなくソートしながら追加する

# 実装

1. 入力を整形して格納する(ex1のinput_info関数を利用する)
2. 前述のアルゴリズムに従ってintersectionsリストに交点を格納
3. 適切に出力する
"""

# テスト用のテキストファイルから入力を得る関数
# 引数pathに入力ファイルパスを渡す
def input_from_file(path="/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/input.txt"):
    with open(path, "r") as f:
        tmp = f.readlines()
        N, M, P, Q = [int(x) for x in tmp[0].replace("\n", "").split(" ")]
        points = []
        segments = []
        roots = []
        for i in range(1, N+1):
            points.append(
                ex1.point([int(x)
                           for x in tmp[i].replace("\n", "").split(" ")])
                )
        for j in range(N+1, N+M+1):
            tmp2 = [int(x) for x in tmp[j].replace("\n", "").split(" ")]
            segments.append(ex1.segment([
                points[tmp2[0]-1],
                points[tmp2[1]-1]
            ]))
        for k in range(N+M+1, N+M+Q+1):
            # 詳しい使い方が不明なのでとりあえずpointsに追加だけする
            adds = [int(x) for x in tmp[k].replace("\n", "").split(" ")]
            points.append(ex1.point(adds))
        for l in range(N+M+P+1, N+M+P+Q+1):
            roots.append([x for x in tmp[l].replace("\n", "").split(" ")])

    return N, M, P, Q, points, segments, roots


def find_all_intersections(M, segments):
    intersections = []
    for i in range(M):
        for j in range(i, M):
            tmp = ex1.find_intersection(segments[i], segments[j])
            if tmp[0]:  # 交点あり
                # print(f"check A, {tmp[1].to_str()}")
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
    return intersections


if __name__ == "__main__":
    # N, M, P, Q, points, segments = ex1.input_info()
    N, M, P, Q, points, segments = input_from_file()

    intersections = find_all_intersections(M, segments)

    for p in intersections:
        print(f"{p.x:.5f} {p.y:.5f}")
