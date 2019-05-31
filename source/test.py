import sys
import time
import random
import Modules.path as path
sys.path.append(path.module_path)
import manager

args = sys.argv
length = len(args)

conditions = {}

conditions["ex1"] = {
    "N": [3, 4],
    "M": [2, 2],
    "P": [0, 0],
    "Q": [0, 0],
    "x": [0, 1000],
    "y": [0, 1000],
    "K": [0, 0]
}

conditions["ex2"] = {
    "N": [2, 200],
    "M": [1, 100],
    "P": [0, 0],
    "Q": [0, 0],
    "x": [0, 1000],
    "y": [0, 1000],
    "K": [0, 0]
}

conditions["ex3"] = {
    "N": [2, 1000],
    "M": [1, 500],
    "P": [0, 0],
    "Q": [0, 100],
    "x": [0, 10**4],
    "y": [0, 10**4],
    "K": [1, 1]
}

conditions["ex4"] = {
    "N": [2, 1000],
    "M": [1, 500],
    "P": [0, 0],
    "Q": [0, 100],
    "x": [0, 10**4],
    "y": [0, 10**4],
    "K": [1, 1]
}

conditions["ex5"] = {
    "N": [2, 1000],
    "M": [1, 500],
    "P": [0, 0],
    "Q": [0, 100],
    "x": [0, 10**4],
    "y": [0, 10**4],
    "K": [1, 10]
}

conditions["ex6"] = {
    "N": [2, 1000],
    "M": [1, 500],
    "P": [0, 0],
    "Q": [0, 100],
    "x": [0, 10**4],
    "y": [0, 10**4],
    "K": [1, 10]
}

conditions["ex7"] = {
    "N": [2, 1000],
    "M": [1, 500],
    "P": [0, 100],
    "Q": [0, 0],
    "x": [0, 10**4],
    "y": [0, 10**4],
    "K": [0, 0]
}

conditions["ex8"] = {
    "N": [2, 2000],
    "M": [1, 1000],
    "P": [0, 0],
    "Q": [0, 0],
    "x": [0, 10**5],
    "y": [0, 10**5],
    "K": [0, 0]
}


def makeTestData(condition):
    datas = {}
    datas["points"] = []
    datas["segments"] = []
    datas["add_points"] = []
    datas["roots_index"] = []

    """
    datas = {
        "N": N,
        "M": M,
        "P": P,
        "Q": Q,
        "points": [
            [x1, y1],
            ...
            [xN, yN]
        ],
        "segments": [
            [p1, q1],
            [pM, qM],
        ],
        "add_points": [
            [x1, y1],
            ...
            [xP, yP]
        ],
        "roots_index":[
            [start1, fin1, K1]
            [startQ, finQ, KQ]
        ]
    }
    """
    for index in ["N", "M", "P", "Q"]:
        tmp = condition[index]
        datas[index] = random.randint(tmp[0], tmp[1])

    for i in range(0, datas["N"]):
        tmp = condition["x"]
        x = random.randint(tmp[0], tmp[1])
        tmp = condition["y"]
        y = random.randint(tmp[0], tmp[1])
        datas["points"].append([x, y])

    for i in range(0, datas["M"]):
        # 線分のPQに交点は選ばない
        p = random.randint(1, datas["N"])
        q = random.randint(1, datas["N"])
        datas["segments"].append([p, q])

    for i in range(0, datas["P"]):
        tmp = condition["x"]
        x = random.randint(tmp[0], tmp[1])
        tmp = condition["y"]
        y = random.randint(tmp[0], tmp[1])
        datas["add_points"].append([x, y])

    for i in range(0, datas["Q"]):
        tmp = condition["K"]
        start = random.randint(1, datas["N"]+1)
        fin = random.randint(1, datas["N"])
        # 交差点は選ばない
        K = random.randint(tmp[0], tmp[1])
        datas["roots_index"].append([start, fin, K])

    return datas


def write_data_to_file(data, path=path.input_path):
    lines = []
    lines.append(f"{data['N']} {data['M']} {data['P']} {data['Q']}")

    for i in range(data["N"]):
        lines.append(f"{data['points'][i][0]} {data['points'][i][1]}")

    for i in range(data["M"]):
        lines.append(f"{data['segments'][i][0]} {data['segments'][i][1]}")

    for i in range(data["P"]):
        lines.append(f"{data['add_points'][i][0]} {data['add_points'][i][1]}")

    for i in range(data["Q"]):
        lines.append(f"{data['roots_index'][i][0]} {data['roots_index'][i][1]} {data['roots_index'][i][2]}")

    with open(path, "w") as f:
        for line in lines:
            f.write(line+"\n")


def measure_run_time(ex):
    M = manager.Manager()
    time1 = time.time()
    M.input2(file=True, path=path.input_path)
    time2 = time.time()
    print(f"入力情報を受け取りました(時間: {time2-time1:.8f}秒)")
    M.find_all_intersections()
    time3 = time.time()
    print(f"全交差点を算出しました(時間: {time3-time2:.8f}秒)")
    M.run(ex)
    time4 = time.time()
    print(f"プログラムの実行が終了しました(時間: {time4-time3:.8f}秒)")
    print(f"合計時間: {time4-time1:.8f}秒")


if __name__ == "__main__":
    """
    python test.py <課題番号> <データ数>
    """

    if length == 3:  # 正常実行
        if args[1].isdigit() and args[2].isdigit():
            ex = int(args[1])
            data_num = int(args[2])
        else:
            print("引数エラー(型)")
            exit

        for i in range(data_num):
            data = makeTestData(conditions[f"ex{ex}"])
            write_data_to_file(data)
            print("テストデータの準備が完了.")
            print("プログラムを実行します.")
            measure_run_time(ex)
            # M.plot()
            # write_data_to_file(data)

    else:
        print("引数エラー(数)")
