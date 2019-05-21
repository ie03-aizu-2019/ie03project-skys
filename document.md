# 道路建設計画支援システムドキュメント

## 目次

- [システムの概要](#chapter1)
- [動作環境](#chapter2)
- [基本的な利用方法](#chapter3)
    - [main.pyからの利用](#chapter3-1)
    - [test.pyからの利用](#chapter3-2)
- [optionについて](#about-option)
- [提供される機能](#chapter4)


<a id="chapter1"></a>

## システムの概要

本システムでは、機能として断片的な道の情報からの道路網復元と、道路網上の経路検索システム、新たな地点につなぐための最適な道の提案機能、重要性の高い道の検出機能を提供します。


システムのTree構造は以下の通りです(一部システムに無関係のファイル, ディレクトリは除いてあります).

``` sh
<BASEDIR>
├── README.md               # README
├── document.html           # このドキュメント
├── main.py                 # システムの利用に使う①
├── Modules
│   ├── input.py
│   ├── manager.py
│   ├── path.py
│   ├── plot.py
│   ├── segments.py
│   └── test.py            # システムの利用に使う②
├── Reports                 # 週刊レポート
│   ├── report0X.md
│   └── template.md
└── static
    ├── figure.png          # 情報の2次元グラフ
    ├── input.txt           # ①のデータ入力に使うテキストファイル
    └── testdata            # ②のデータ入力に使うフ複数ファイルのディレクトリ
        └── testdata<小課題番号>-<N>.txt
```

このドキュメントでは, 基本的に \<BASEDIR\> をルートディレクトリとしてファイルパスを書いていきます.

<a id="chapter2"></a>

## 動作環境

動作環境として,

- Python 3.7.2
- Mac OS

を想定します.

新しめのPython3系さえあれば動作すると思いますが, 一部グラフ化等の機能が制限されれる可能性があります.

<a id="chapter3"></a>

## 基本的な利用方法

システムの利用方法は2種類用意されています.

1. **./main.py** から利用する
2. **./Modules/test.py** から利用する

<a id="chapter3-1"></a>

### ① ./main.py から利用する

main.py では, 入力から出力を得るだけのシンプルな機能を提供します.

``` sh
python ./main.py <input_option> <output_option>
```

※ \<input_option\>と\<output_option\>については, [optionについて](#about-option) を参照してください.

<a id="chapter3-2"></a>

### ② ./Modules/test.py

test.pyでは, main.pyで得られるシンプルな出力に加えて, 詳細な地点等の情報や2次元平面図を出力する.

``` sh
python ./Modules/test.py <input_option> <output_option>
```

※ \<input_option\>と\<output_option\>については
, [optionについて](#about-option) を参照してください.

<a id="about-option"></a>

## option について

### ①input_option

input_optionでは, データ入力の方法を指定します.

| input_option | 入力手段 |
| :---: | :--- |
| -i | ターミナルから |
| -f | ./static/input.txt から |

**-f** オプションでファイルから入力する場合は, 予め入力データを **./static/input.txt** に入力しておく必要があります.

### ②output_option

output_optionでは, 入力されたデータに対して如何なる処理をした結果を出力するかを指定します.

| output_option | 出力 |
|:---:|:---|
| 1 | 2線分の交点座標 |
| 2 | 全ての交差点座標 |
| 3 | 最短経路の距離 |
| 4 | 最短経路と距離 |
| 5 | 第K番目までの経路の距離 |
| 6 | 第K番目までの経路と距離 |
| 7 | 最適な交差点座標 |
| 8 | 幹線道路 |

<a id="chapter4"></a>

## 提供される機能
