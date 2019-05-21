"""
python test.py <入力方法> <課題番号>

<入力方法>
1. -i : 手入力
2. -f : 予め用意されたテストデータを使う

<課題番号>
整数で小課題番号を渡せば良い
"""

import manager
import os
import sys
import random

M = manager.Manager()

args = sys.argv
length = len(args)
root_path = "../static/testdata/"

# ⇓進展次第変更
ex_info = {
    # 小課題番号: [実装済みかどうか, テストデータリスト]
    1: [True, ["1-1", ]],
    2: [True, []],
    3: [True, []],
    4: [True, []],
    5: [False, []],
    6: [False, []],
    7: [False, []],
    8: [False, []],
}
sample = """# Sample(小課題2をテストデータから実行)
$ python test.py -f 2"""


def test(ex, file=True):
    """
    ex:   小課題番号
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
        index = random.randint(0, len(ex_info[ex][1])-1)
        path = f"{root_path}testdata{ex_info[ex][1][index]}.txt"
        if os.path.exists(path):
            # 正常実行
            print(f"# 小課題{ex}のテスト実行\n")
            M.input(file=file, path=path)
            print(f"# 今回使用したテストデータ: testdata{ex_info[ex][1][index]}.txt⇓")
            with open(path, "r") as f:
                for line in f.readlines():
                    print(line, end="")
            print("\n# 詳細データ")
            M.print_info(detail=True)
            print(f"\n# 小課題{ex}の実行")
            if ex == 1:
                M.ex1()
            elif ex == 2:
                M.ex2()
            elif ex == 3:
                M.ex3()
            elif ex == 4:
                M.ex4()
            # elif ex == 5:
            #     M.ex5()
            # elif ex == 6:
            #     M.ex6()
            # elif ex == 7:
            #     M.ex7()
            # elif ex == 8:
            #     M.ex8()
            return True
        else:
            print(f"該当するテストデータが存在しません.")
            return False
    pass


if __name__ == "__main__":
    if length == 3:  # test.py, -i/-f, n
        if args[1] in ["-i", "-f"] and args[2].isdigit:
            # 正常な引数 => 実行
            file = True
            if args[1] == "-i":
                file = False
            n = int(args[2])
            result = test(n, file=file)
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
