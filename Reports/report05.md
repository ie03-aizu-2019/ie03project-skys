# Progress Report : Week 5

**Team: SKYS**

**Class Date: 05/14**

**URL** : https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report05.md

##  各課題の見通し

### 小課題5

Manager.roots[始点インデックス][終点インデックス]に, リスト形式でソートされたルート情報があるので, 第K番目を取得して, 小課題3と同じように出力することで完成見込み.

### 小課題6

小課題5と同様に第K番目を取得して, 小課題4と同じように出力することで完成見込み.

### 小課題7

新たに点を追加する必要ができたので, まずは入力を修正する必要がある. 追加点情報をManagerクラスで取得できるように修正する必要がある.

追加地点からもっとも近い道を道路網につないでいくという課題だが, 線分に対してもっとも近い線分を接続するための交点を求める関数は, segments.calc_shortest_connection() に実装してあるので, これを全ての線分に対して実行して, もっとも距離が短いものに繋ぐことで実装できる.

ゆえに, 実装のためのTo DOは

1. input.input_from_stdin() と input.input_from_file()の修正とそれに伴い, Managerクラスで追加点情報を受け取れるようにする
2. segments.calc_shortest_connection()を利用して, 全ての線分のなかでもっとも近い線分を引ける線分を求める関数の定義
3. 2の関数の実行後, その線分と交点をManager.segmentsとManager.pointsに追加する処理をなんらかの方法で追加(点と線分に対する追加メソッドをそれぞれ定義するのが良さげ. 接点情報もしっかり更新できるようにする)
4. 適切に出力する(出力する関数は, Manager.ex7()にする)

> 最小の⻑さの道の候補が複数ある場合、より先にある 道の方につなぐ
との記述があるが, "より先にある"の定義がよくわからないのでとりあえず最小の道の候補が複数ある時の処理は保留にしておく.

### 小課題8

Managerクラスは各始点インデックス→終点インデックスの経路情報(線分)を全て持っているので, 幹線道路の定義が **点Pから点Qへ行くのに必ず通らなければならない線分** であるなら, 共通で通る線分を取得するだけなので実装自体は容易である(集合で比較しても良いし, 普通にループを回してもOK)

ただ, 総Root数は結構エグい量なので効率化のためになんらかの工夫をしたほうが良いかもしれない.

実装方法と効率化のための工夫は越川くんに任せる.


## 各メンバーの作業

### s1250131 木村:

フェーズ1において各小課題ごとにexX.pyファイルを作っていたせいで各関数やクラスがどこにあるか非常にわかりづらくなってしまったので, Modulesディレクトリに複数のPythonスクリプトファイルを生成し, 用途ごとに全てのソースコードを分割して移行した.

今後は, 各フェーズのフォルダからはmain関数の実行を行い, 中身の処理はModulesディクレクトリのファイルに追記, あるいは新規ファイルを作成して記述していくことにする.

今週の作業は,

- ソースコードの移行
- サードパーティ製モジュールのmatplotlibを使い, 点と交点と線分を2次元平面上にプロットして可視化するプログラムの実装.
- Managerクラスのprint_info()の修正
- ルート探索をするManager.search_root()で, ソートはされていたが同じルートを複数回格納しているバグがあったので修正した. これによりManagerクラスで小課題5と小課題6に必要な情報は全て持っているので, 出力をいじるだけで完成する見込みである

をした.

### s1250133 越川:

メンバーが行った作業内容について書く。
たとえば、どの処理を実装したか、こういう入力に対してこう対応したとか、こういうテストデータを作ったとか、環境設定を行ったなど。