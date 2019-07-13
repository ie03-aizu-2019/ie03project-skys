"""
python main2.py <入力方法> <課題番号> <case番号>

<入力方法>
1. -i : 手入力
2. -f : 予め用意されたテストデータを使う

<課題番号>
整数で小課題番号を渡せば良い
"""

import sys
import os
import Modules.path as path
# sys.path.append(path.module_path)
import test

args = sys.argv
length = len(args)

# ⇓進展次第変更
ex_info = {
    # 小課題番号: [実装済みかどうか, テストデータリスト]
    1: [True, ["1-1", "1-2", "1-3", "1-4"]],
    2: [True, ["2-1", "2-2", "2-3", "2-4"]],
    3: [True, ["3-1", "3-2", "3-3", "3-4"]],
    4: [True, ["4-1", "4-2", "4-3", "4-4"]],
    5: [True, ["5-1", "5-2", "5-3", "5-4"]],
    6: [True, ["6-1", "6-2", "6-3", "6-4"]],
    7: [True, ["7-1", "7-2", "7-3"]],
    8: [False, ["8-2", "8-3"]],
    9: [True, ["9-1"]],
}
sample = """# Sample(小課題2をテストデータから実行)
$ python test.py -f 2"""


def main2(ex, case, file=True):
    """
    ex:   小課題番号
    case: ケース番号
    file: テストデータファイルを使うか否か
    """
    if ex not in list(ex_info):
        print(f"小課題{ex}は存在しません.")
        return False
    elif not ex_info[ex][0]:
        print(f"小課題{ex}はまだ実装されていません.")
        return False
    elif not len(ex_info[ex][1]):
        print(f"小課題{ex}のテストデータはまだ用意されていません.")
        return False
    else:
        index = case
        datapath = f"{path.testdata_path}/testdata{ex_info[ex][1][index-1]}.txt"
        if os.path.exists(datapath):
            # 正常実行
            print(f"# 今回使用するテストデータ: testdata{ex_info[ex][1][index-1]}.txt⇓")
            with open(datapath, "r") as f:
                for line in f.readlines():
                    print(line, end="")
            print(f"\n# 小課題{ex}の実行")
            M = test.measure_run_time(ex, path=datapath)
            print("\n# 詳細データ")
            M.print_info(length=1)

            print("\n# プロット図の表示")
            M.plot()
            return True
        else:
            print(f"該当するテストデータが存在しません.")
            return False
    pass


if __name__ == "__main__":
    if length == 4:  # test.py, -i/-f, n, case
        if args[1] in ["-i", "-f"] and args[2].isdigit and args[3].isdigit:
            # 正常な引数 => 実行
            file = True
            if args[1] == "-i":
                file = False
            n = int(args[2])
            case = int(args[3])

            result = main2(n, case, file=file)
            if result:
                print("プログラムを正常終了します.")
            else:
                print("プログラムを終了します.")
        else:
            # 引数が未定義
            print(f"[ERROR]未定義の引数です.\n{sample}")
    else:
        # 引数の長さが異なる
        print(f"[ERROR]引数の数が異なります.\n{sample}")
