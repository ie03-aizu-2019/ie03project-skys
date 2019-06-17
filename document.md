# 道路建設計画支援システムドキュメント

## 目次

- [システムの概要](#chapter1)
- [実行環境とビルド方法](#chapter2)
- [基本的な利用方法](#chapter3)
    - [main.pyからの利用](#chapter3-1)
    - [main2.pyからの利用](#chapter3-2)
- [optionについて](#about-option)


<a id="chapter1"></a>

## システムの概要

本システムでは、機能として断片的な道の情報からの道路網復元と、道路網上の経路検索システム、新たな地点につなぐための最適な道の提案機能、重要性の高い道の検出機能を提供します。


プログラムのソースは, sourceディレクトリにあります.

``` sh
source
├── Modules
│   ├── input.py
│   ├── manager.py
│   ├── path.py
│   ├── plot.py
│   ├── segments.py
│   └── test.py
├── main.py
├── setup.py
└── static
    ├── figure.png
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
$ python3 setup.py
```

｢正常にセットアップが完了しました｣と表示されれ, 環境構築は終了です.

<a id="chapter3"></a>

## 基本的な利用方法

システムの利用方法は2種類用意されています.

1. **source/main.py** から利用する
2. **source/main2.py** から利用する

<a id="chapter3-1"></a>

### ① source/main.py から利用する

main.py では, 入力から出力を得るだけのシンプルな機能を提供します.

``` sh
python source/main.py <input_option> <ex_num>
```

入力ファイルは, **source/static/input.txt** に用意する必要があります.

※ \<input_option\>と\<ex_num\>については, [optionについて](#about-option) を参照してください.

<a id="chapter3-2"></a>

### ② source/main2.py

main2.pyでは, main.pyで得られるシンプルな出力に加えて, 詳細な地点等の情報や2次元平面図を出力する.

``` sh
python source/main2.py <input_option> <ex_num> <case_num>
```

テストデータは予め用意されています.

※ \<input_option\>と\<ex_num\> \<case_num\>については
, [optionについて](#about-option) を参照してください.

<a id="about-option"></a>

## option について

### ①input_option

input_optionでは, データ入力の方法を指定します.

| input_option | 入力手段 |
| :---: | :--- |
| -i | ターミナル入力 |
| -f | ファイル入力 |

**-f** オプションでmain.pyを実行する場合は, 予め入力データを **source/static/input.txt** に入力しておく必要があります.

### ② ex_num

output_optionでは, 入力されたデータに対して実行する処理を小課題番号で指定します.

### ③ case_num

case_num では, テストケースの番号を入力します.

| オプション | テストケース |
|:---:|:---:|
| 1 | 通常ケース |
| 2 | 最小入力ケース |
| 3 | 最大入力ケース |
| 4以降 | 特殊ケース |
