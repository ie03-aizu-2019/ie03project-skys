# Progress Report : Week 2

**Team: SKYS**

**Class Date: 04/17**

**URL** : https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report02.md


## 小課題2

- 小課題1で定義したsegmentクラスとpointクラスを利用
- 小課題1で定義したinput_info関数で入力を得る

入力されたsegment数Mに対して,

for i in [0, ..., M-1]:
    for j in [i+1, M-1]:
        intersections.append(find_intersection())

して全ての交差点リストを得る
※実際には, append(末尾から追加)ではなくソートしながら追加する


1. 入力を整形して格納する(ex1のinput_info関数を利用する)
2. 前述のアルゴリズムに従って全ての交差点を取得し, intersectionsリストにソートされた状態で格納する
3. 適切に出力する


## 各メンバーの作業

### s1250131 木村:

- 小課題1においてBPMを定義して, find_intersection関数を完成させた.
- 小課題2の2の全ての交差点を取得して返す関数 find_all_intersections() を実装した.
- 小課題2において入力のテストがターミナルからではめんどうだったのでテスト用にテキストファイルから入力を得る input_from_file 関数を実装した.
- 小課題1で使った input_info 関数で入力を得て, 実装した find_all_intersections関数 を使うことで小課題2を完成させた.


### s1250133 越川:

メンバーが行った作業内容について書く。
たとえば、どの処理を実装したか、こういう入力に対してこう対応したとか、こういうテストデータを作ったとか、環境設定を行ったなど。
