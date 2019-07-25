"""
関数
- input_from_stdin()
- input_from_file(path)
"""

import segments as sg
# segmentsモジュールをsegとして使える
import path
# 標準ライブラリpathをインポート


def input_from_stdin():
    # 修正したinput_infoを移行する
    points = []
    segments = []

    tmp = input("")  # "4 2 0 0"
    tmp = tmp.split(" ")  # ["4", "2", "0", "0"]
    # tmpに文字型の数字を格納。
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i])
    # [4, 2, 0, 0]
    N, M, P, Q = tmp
    # N = tmp[0] , M = tmp[1] , P = tmp[2] , Q = tmp[3]
    for i in range(N):  # for N回まわしてなかでinput
        tmp = input("")
        tmp = tmp.split(" ")  # "0 0" -> ["0", "0"]
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        # point([0, 0])
        points.append(sg.point(tmp))  # points.append(point(koshikawa))

    for i in range(M):  # for m
        tmp = input()
        tmp = tmp.split(" ")
        # "0 0" ->  koshikawa = [0, 0]
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        segments.append(
            sg.segment([points[tmp[0]-1], points[tmp[1]-1]]))
        # segments.append(segment(koshikawa))

        """
        roots [
            ["1", "4", 1],
            ["C1", "3", 1]
        ]
        """

    roots = []

    add_points = []
    for i in range(P):
        tmp = input("")
        tmp = tmp.split(" ")
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        add_points.append(sg.point(tmp))

    for i in range(Q):
        tmp = input("")
        tmp = tmp.split(" ")
        tmp[2] = int(tmp[2])
        # tmp = ["1", "4", 1]
        roots.append(tmp)

    for i in range(Q):
        tmp = input("")
        tmp = tmp.split(" ")
        roots[i] = tmp
        roots[i][2] = int(tmp[i][2])

    return N, M, P, Q, points, segments, add_points, roots


def input_from_file(path=path.input_path):
    with open(path, "r") as f:
        tmp = f.readlines()
        N, M, P, Q = [int(x) for x in tmp[0].replace("\n", "").split(" ")]
        points = []
        segments = []
        roots = []
        add_points = []

        for i in range(1, N+1):  # points
            points.append(
                sg.point([int(x)
                          for x in tmp[i].replace("\n", "").split(" ")])
                )
        for j in range(N+1, N+M+1):  # segments
            tmp2 = [int(x) for x in tmp[j].replace("\n", "").split(" ")]
            segments.append(sg.segment([
                points[tmp2[0]-1],
                points[tmp2[1]-1]
            ]))
        for k in range(N+M+1, N+M+P+1):  # add points
            # 詳しい使い方が不明なのでとりあえずpointsに追加だけする
            adds = [int(x) for x in tmp[k].replace("\n", "").split(" ")]
            add_points.append(sg.point(adds))
        for l in range(N+M+P+1, N+M+P+Q+1):  # root
            roots.append([x for x in tmp[l].replace("\n", "").split(" ")])

    return N, M, P, Q, points, segments, add_points, roots
