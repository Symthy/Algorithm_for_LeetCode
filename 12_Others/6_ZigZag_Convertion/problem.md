# Problem

文字列"PAYPALISHIRING"は、次のように特定の行数にジグザグパターンで書き込まれます (読みやすくするために、このパターンを固定フォントで表示することもできます) 。

```py
  def convert(self, s, numRows):
    if numRows == 1:
      return s

    curRow, step = 0, 1
    rows = [''] * numRows

    for ch in s:
      rows[curRow] += ch
      if curRow == numRows - 1:
        step = -1
      elif curRow == 0:
        step = 1
      curRow += step

    return ''.join(rows)
```

```
/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
```
