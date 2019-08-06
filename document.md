# 道路建設計画支援システムドキュメント

## 目次

- [システムの概要](#chapter1)
- [実行環境とビルド方法](#chapter2)
- [入力について](#chapter3)
- [基本的な利用方法](#chapter4)
    - [入力ファイルの用意/入力](#chapter4-1)
    - [システムの利用(統合版)](#chapter4-2)
    - [出力の見方](#chapter4-3)
    - [各小課題を解く](#chapter4-4)
- [source/main.pyでの実行](#chapter5)
- [テストデータ生成器について](#chapter6)
- [ビジュアライザの不具合について](#chapter7)

<a id="chapter1"></a>

## システムの概要

本システムでは入力から道路網を構築し, ある地点からある地点への経路探索や新たな地点を適切に追加して道路網の更新等を可能にします.

プログラムのソースは, sourceディレクトリにあります.

``` sh
source
├── Modules
│   ├── input.py
│   ├── manager.py
│   ├── path.py
│   ├── plot.py
│   ├── segments.py
├── main.py
├── main2.py
├── setup.py
├── test.py
└── static
    ├── input.txt
    ├── requirements.txt
    └── testdata
        └── testdataα-β.txt
```

<a id="chapter2"></a>

## 実行環境とビルド方法

実行環境として,

- [Python 3.7.2](https://www.python.org/downloads/release/python-372/)
- Mac OS

を想定します(WindowsやUnixだとプロット図の表示でエラーが発生する可能性が高い).

その他必要なモジュールのインストールは, **setup.py** で行います.

``` sh
$ git clone git@github.com:ie03-aizu-2019/ie03project-skys.git
$ python3 setup.py
```

｢正常にセットアップが完了しました｣と表示されれ, 環境構築は終了です.

<a id="chapter3"></a>

## 入力について

内容後でかく

<a id="chapter4"></a>

## 基本的な利用方法

システムの利用方法は,

1. **source/main.py**
2. **source/main2.py**

の2種類が用意されていますが, より分かりやすいmain2.pyを推奨します.

<a id="chapter4-1"></a>

### ① 入力ファイルの用意/入力

``` markup
- input.txtから入力を渡せるように修正
- testdataについて説明
- 手入力について説明
```

<a id="chapter4-2"></a>

### ② システムの利用(統合版)

``` sh
$ cd path/to/source
$ python3 main2.py -f 9 1
```

を実行することで, システムを利用できます.


``` markup
- Ex9のP, Qの条件分岐等を説明する
```

<a id="chapter4-3"></a>

### ③ 出力の見方

``` markup
- 出力例を提示して, 各部分がなにを表しているのか説明する
```

<a id="chapter4-4"></a>

### ④ source/main2.py から各小課題を解く

``` markup
- 各小課題番号が解く課題を説明する
- 小課題番号の指定方法等を説明する
```

<a id="chapter5"></a>

## source/main.py の利用

``` markup
- 一応一通りmain.pyの使い方も乗せる
- ほぼmain2.pyと同じだからざっくりでおけ
```

<a id="chapter6"></a>

## テストデータ生成器

``` markup
test.pyでテストデータ生成ができるからこれについて一通りまとめる
```

<a id="chapter7"></a>

## プロット不具合

``` markup
- プロットに不具合が結構あって, 解決するにはmatplotlibrc?みたいいなやつをいじる
- 適当に書いといて
```

``` markup
あと必要そうなの思いついたら好きに項目つけて書いといて❢
```
