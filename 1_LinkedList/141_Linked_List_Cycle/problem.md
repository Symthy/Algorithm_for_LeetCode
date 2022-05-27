# Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

Type：Linked List

# 問題
リンクリストの先頭であるheadが与えられたとき、そのリンクリストにサイクルがあるかどうかを判定せよ。

リンクリストにサイクルが存在するのは、リスト内に次のポインタを追い続けることで再び到達できるノードがある場合である。内部的には、posはtailの次のポインタが接続されているノードのインデックスを示すために使用される。posはパラメータとして渡されないことに注意。

リンクリストにサイクルが存在する場合はtrueを返す。そうでなければ、falseを返す。


# 解説

知ってないと解けない

slow：１つ先に進む
fast：２つ先に進む

cycle があれば、fast が必ずslowに追いつく寸法
