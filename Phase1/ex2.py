# コメントアウトしといて
import sys
sys.path.append("/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/")
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
