"""
input.txtからの実行用
python main.py -f 1
"""
import sys
import Modules.path as path
sys.path.append(path.module_path)
import manager

M = manager.Manager()
import test

args = sys.argv
length = len(args)

sample = """# Sample(小課題2をテストデータから実行)
$ python main.py -f 2"""

if __name__ == "__main__":
    if length == 3:  # main.py, -i/-f, n
        if args[1] in ["-i", "-f"] and args[2].isdigit:
            # 正常な引数 => 実行
            file = True
            if args[1] == "-i":
                file = False
            n = int(args[2])
            M.input(file=file, path=path.input_path)
            M = manager.Manager()
            M.input(file=True, path=path.input_path)
            M.run(n)
            # M.print_info()
            # test.measure_run_time(n)
        else:
            # 引数が未定義
            print(f"[ERROR]未定義の引数です.\n{sample}")
    else:
        # 引数の長さが異なる
        print(f"[ERROR]引数の数が異なります.\n{sample}")
