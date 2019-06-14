import sys
import time
import random
import Modules.path as path
sys.path.append(path.module_path)
import manager

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


def makeTestData(condition, options={}):
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
        diff = tmp[1] - tmp[0]
        diff *= 0.1
        diff = int(diff)
        datas[index] = random.randint(tmp[0], tmp[0]+diff)
        if index in list(options):
            datas[index] = options[index]

    if datas["M"] > datas["N"]//2:
        datas["M"] = random.randint(tmp[0], datas["N"]//2)


    for i in range(0, datas["N"]):
        tmp = condition["x"]
        x = random.randint(tmp[0], tmp[1])
        tmp = condition["y"]
        y = random.randint(tmp[0], tmp[1])
        datas["points"].append([x, y])

    for i in range(0, datas["M"]):
        # 線分のPQに交点は選ばない
        count = 0
        while(True):
            # 始点と終点が同じ点になった場合はやり直す
            p = random.randint(1, datas["N"])
            q = random.randint(1, datas["N"])
            if [p, q] in datas["segments"]:
                count += 1
                continue
            elif count > 5:
                break
            elif p == q:
                count += 1
                continue
            else:
                break
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


class generetor:
    def __init__(self):
        self.current_data = None

    def setex(self, ex):
        self.ex = ex

    def makedata(self, type):
        """
        None 通常ケース(資料のものをコピー)
        min minケース(Nが制約での最小値)
        max maxケース(Nが制約での最大値)
        None 例外ケース(個別に手動で作る)
        """
        condition = conditions[f"ex{self.ex}"]
        options = {}
        if type == "min":
            options["N"] = condition["N"][0]
        elif type == "max":
            options["N"] = condition["N"][1]
        self.current_data = makeTestData(condition, options)

    def write_to_testdata(self, op):
        tpath = path.testdata_path
        tpath = f"{tpath}/testdata{self.ex}-{op}.txt"
        write_data_to_file(self.current_data, path=tpath)

    def write_min_max_testdata(self):
        for i in range(1, 9):
            self.setex(str(i))
            self.makedata("min")
            self.write_to_testdata("2")
            self.makedata("max")
            self.write_to_testdata("3")



if __name__ == "__main__":
    """
    python test.py <課題番号>
    """
    gen = generetor()
    gen.write_min_max_testdata()
