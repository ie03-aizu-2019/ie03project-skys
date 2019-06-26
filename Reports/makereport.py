import sys

args = sys.argv
# args[0] = makereport.py
# args[1] = ex
# args[2] = month
# args[2] = date

ex = int(args[1])
month = int(args[2])
date = int(args[3])

file_name = f"report{ex:0>2}.md"
template = f"""
# Progress Report : Week {ex}

**Team: SKYS**

**Class Date: {month:0>2}/{date:0>2}**

**URL** : https://github.com/ie03-aizu-2019/ie03project-skys/tree/master/Reports/report{ex:0>2}.md


各課題の実装方針や、必要と思われるその他作業の見積もりなど。


## 各メンバーの作業

### s1250131 木村:

メンバーが行った作業内容について書く。
たとえば、どの処理を実装したか、こういう入力に対してこう対応したとか、こういうテストデータを作ったとか、環境設定を行ったなど。


### s1250133 越川:

メンバーが行った作業内容について書く。
たとえば、どの処理を実装したか、こういう入力に対してこう対応したとか、こういうテストデータを作ったとか、環境設定を行ったなど。
"""

if __name__ == "__main__":
    with open(file_name, 'w') as f:
        f.write(template)
