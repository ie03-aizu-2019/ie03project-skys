"""
<入力方法>
1. -i : 手入力
2. -td : 予め用意されたテストデータを使う
3. -f : input.txtをテストデータとして使う

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

ex_info = {
    # 小課題番号: [実装済みかどうか, テストデータリスト]
    1: [True, ["1-1", "1-2", "1-3", "1-4"]],
    2: [True, ["2-1", "2-2", "2-3", "2-4"]],
    3: [True, ["3-1", "3-2", "3-3", "3-4"]],
    4: [True, ["4-1", "4-2", "4-3", "4-4"]],
    5: [True, ["5-1", "5-2", "5-3", "5-4"]],
    6: [True, ["6-1", "6-2", "6-3", "6-4"]],
    7: [True, ["7-1", "7-2", "7-3"]],
    8: [True, ["8-1", "8-2", "8-3", "8-4", "8-5"]],
    9: [True, ["9-1", "9-2", "9-3", "9-4", "9-5", "9-6", "9-7"]],
    10: [True, ["10-1", "10-2", "10-3"]],
    11: [True, ["11-1", "11-2", "11-3"]],
}
sample = """# Sample(小課題2をテストデータから実行)
$ python test.py -td 2"""


def main2(ex, case=None, file=True, inpath=None, length=30):
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
        datapath = None
        if case is not None:
            datapath = f"{path.testdata_path}"
            datapath = f"{datapath}/testdata{ex_info[ex][1][index-1]}.txt"
        if inpath is None and datapath is not None:
            inpath = datapath
        if not file:
            print(f"\n# 小課題{ex}の実行")
            M = test.measure_run_time(ex, file=file, path=inpath)
            print("\n# 詳細データ")
            M.print_info(length=length)

            print("\n# プロット図の表示")
            M.plot()
            return True
        elif os.path.exists(inpath):
            # 正常実行
            # print(f"# 今回使用するテストデータ: testdata{ex_info[ex][1][index-1]}.txt⇓")
            with open(inpath, "r") as f:
                for line in f.readlines():
                    print(line, end="")
            print(f"\n# 小課題{ex}の実行")
            M = test.measure_run_time(ex, file=file, path=inpath)
            print("\n# 詳細データ")
            M.print_info(length=length)

            print("\n# プロット図の表示")
            M.plot()
            return True
        else:
            print(f"該当するテストデータが存在しません.")
            return False
    pass


if __name__ == "__main__":
    if length == 4:  # test.py, -td, n, case
        if args[1] in ["-td"] and args[2].isdigit and args[3].isdigit:
            # 正常な引数 => 実行
            file = True
            inpath = None
            if args[1] == "-td":
                inpath = path.input_path
            n = int(args[2])
            case = int(args[3])

            result = main2(n, case, file=file, inpath=inpath)
            if result:
                print("プログラムを正常終了します.")
            else:
                print("プログラムを終了します.")
        else:
            # 引数が未定義
            print(f"[ERROR]未定義の引数です.\n{sample}")
    elif length == 3:  # -i, -f
        if args[1] in ["-i","-f"] and args[2].isdigit:
            # 正常な引数 => 実行
            file = True
            inpath = None
            if args[1] == "-i":
                file = False
            if args[1] == "-f":
                inpath = path.input_path
            n = int(args[2])
            result = main2(n, case=None, file=file, inpath=inpath)
            if result:
                print("プログラムを正常終了します.")
            else:
                print("プログラムを終了します.")
        else:
            print(f"[ERROR]未定義の引数です.¥n{sample}")
    else:
        # 引数の長さが異なる
        print(f"[ERROR]引数の数が異なります.\n{sample}")
