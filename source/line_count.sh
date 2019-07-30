#!/bin/sh

KIMURA="s1250131_Kimura"
KOSHIKAWA="s1250133_koshikawa"

ka1=`ls | grep py | xargs -n1 git --no-pager blame -f -w| grep $KIMURA |wc -l`
ko1=`ls | grep py | xargs -n1 git --no-pager blame -f -w| grep $KOSHIKAWA |wc -l`
cd Modules
ka2=`ls | grep py | xargs -n1 git --no-pager blame -f -w| grep $KIMURA |wc -l`
ko2=`ls | grep py | xargs -n1 git --no-pager blame -f -w| grep $KOSHIKAWA |wc -l`

echo $(($ka1+$ka2))
echo $(($ko1+$ko2))
