# Problem

文字列 s と文字列 wordDict のディクショナリを指定すると、s を 1 つ以上のディクショナリ単語のスペース区切りのシーケンスにセグメント化できる場合に true を返します。

ディクショナリ内の同じ単語は、セグメント化で複数回再利用できることに注意してください。

# Ans

```py
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    d = [False] * len(s)
    for i in range(len(s)):
        for w in wordDict:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]
```

dp の中身は返すものに合わせた方がいい？
