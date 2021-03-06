# ie03project-skys

## 授業に関するリンク

- [Integrated Exercise for Software I](http://web-int.u-aizu.ac.jp/course/ie-soft1/)
- [演習イントロダクション](http://web-int.u-aizu.ac.jp/course/ie-soft1/ISE2019_intro.pdf)
- [リポジトリ](https://github.com/ie03-aizu-2019/ie03project-skys)
- [フェーズ1](http://web-int.u-aizu.ac.jp/course/ie-soft1/ISE2019_phase1.pdf)
- [フェーズ2](http://web-int.u-aizu.ac.jp/course/ie-soft1/ISE2019_phase2.pdf)
- [フェーズ3](http://web-int.u-aizu.ac.jp/course/ie-soft1/ISE2019_phase3.pdf)

## メンバー一覧

- s1250131, [Kaito Kimura](https://github.com/s1250131-Kimura)
- s1250133, [Sora Koshikawa](https://github.com/s1250133-koshikawa)

## 開発環境

- 言語: [Python 3.7.2](https://www.python.org/)
- 管理: [Github](https://github.com/)
- [リポジトリ](https://github.com/ie03-aizu-2019/ie03project-skys)
- エディタ, デバッガ等: [Atom](https://atom.io/)


## ビルド方法

### 1. ソースコードの取得

このGitリポジトリからクローン.

``` sh
$ git clone git@github.com:ie03-aizu-2019/ie03project-skys.git
```

### 2. セットアップ

``` sh
$ cd <クローンしたフォルダ>/source/
$ python3 setup.py
```

### 3. プログラムの実行

``` sh
$ python3 main.py -i 1  # 手入力, 小課題1
$ python3 main2.py -f 2 1  # ファイル入力, 小課題2, テストケース1
```

※ファイルから入力をする場合は, **source/static/input.py** にデータを予め入力した上で, -iオプション を -fオプションに変えて実行します.
※1は小課題番号を表します.


## 成果物

- [ドキュメント](https://htmlpreview.github.io/?https://github.com/ie03-aizu-2019/ie03project-skys/blob/master/document.html)
- [Managerクラス図](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/images/manager.png)
- [主要クラス図](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/images/Segments.png)
- [Modules/(主要なソースコード)](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/source/Modules)
- [test.py(テストデータ生成)](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/source/test.py)
- [main.py(単純実行)](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/source/main.py)
- [main2.py(詳細な実行)](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/source/main2.py)

## 週刊レポート, 中間レビュー, 期末レビュー

### フェーズ1

- [週刊レポート1](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report01.md)
- [週刊レポート2](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report02.md)
- [週刊レポート3](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report03.md)

### フェーズ2

- [週刊レポート4](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report04.md)
- [週刊レポート5](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report05.md)
- [週刊レポート6](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report06.md)
- [週刊レポート7](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report07.md)
- [中間レビュースライド](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/Midterm.pptx)

### フェーズ3

- [週刊レポート8](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report08.md)
- [週刊レポート9](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report09.md)
- [週刊レポート10](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report10.md)
- [週刊レポート11](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report10.md)
- [週刊レポート12](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report10.md)
- [期末レビュースライド](https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/final2.pptx)
