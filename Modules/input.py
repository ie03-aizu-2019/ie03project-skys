"""
関数
- input_from_stdin()
- input_from_file()
"""

import segments as sg


paths = [
    "/Users/kaito/Desktop/今期/synthesis/assignment/Phase1/input.txt",
    "越川のパス"
]
default_path = paths[0]


def input_from_file(path=default_path):
    with open(path, "r") as f:
        tmp = f.readlines()
        N, M, P, Q = [int(x) for x in tmp[0].replace("\n", "").split(" ")]
        points = []
        segments = []
        roots = []

        for i in range(1, N+1):
            points.append(
                sg.point([int(x)
                           for x in tmp[i].replace("\n", "").split(" ")])
                )
        for j in range(N+1, N+M+1):
            tmp2 = [int(x) for x in tmp[j].replace("\n", "").split(" ")]
            segments.append(sg.segment([
                points[tmp2[0]-1],
                points[tmp2[1]-1]
            ]))
        for k in range(N+M+1, N+M+P+1):
            # 詳しい使い方が不明なのでとりあえずpointsに追加だけする
            adds = [int(x) for x in tmp[k].replace("\n", "").split(" ")]
            points.append(sg.point(adds))
        for l in range(N+M+P+1, N+M+P+Q+1):
            roots.append([x for x in tmp[l].replace("\n", "").split(" ")])

    return N, M, P, Q, points, segments, roots
