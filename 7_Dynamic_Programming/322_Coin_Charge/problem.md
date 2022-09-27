# problem

異なる種類のコインを表す整数配列のコインと、合計金額を表す整数値が与えられます。

その金額を補充するために必要な最小数のコインを返します。コインの組み合わせでその金額を構成できない場合は、-1 を返します。

あなたはそれぞれの種類のコインを無限に持っていると思うかもしれません。

## Ans

```py
def coinChange(self, coins: List[int], amount: int) -> int:
    max = amount + 1
    dp = [max] * max
    dp[0] = 0

    for amount_i in range(1, amount+1):
        for coin_i in range(len(coins)):
            if coins[coin_i] <= amount_i:
                dp[amount_i] = min(dp[amount_i], dp[amount_i - coins[coin_i]] + 1)
    return -1 if dp[amount] > amount else dp[amount]
```

example 1:

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

```
M = amount+1

dp:[ 0, M, M, M, M, M, M, M, M, M, M ]

amount_i=1
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
1 [ 0, 1, M, M, M, M, M, M, M, M, M ]
2 [ 0, 1, M, M, M, M, M, M, M, M, M ] 更新なし
5 [ 0, 1, M, M, M, M, M, M, M, M, M ] 更新なし

amount_i=2
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
1 [ 0, 1, 2, M, M, M, M, M, M, M, M ]
2 [ 0, 1, 1, M, M, M, M, M, M, M, M ]
5 [ 0, 1, 1, M, M, M, M, M, M, M, M ] 更新なし

amount_i=3
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
1 [ 0, 1, 1, 2, M, M, M, M, M, M, M ]
2 [ 0, 1, 1, 2, M, M, M, M, M, M, M ]
5 [ 0, 1, 1, 2, M, M, M, M, M, M, M ] 更新なし

amount_i=4
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
1 [ 0, 1, 1, 2, 3, M, M, M, M, M, M ]
2 [ 0, 1, 1, 2, 2, M, M, M, M, M, M ]
5 [ 0, 1, 1, 2, 2, M, M, M, M, M, M ] 更新なし

amount_i=5
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
1 [ 0, 1, 1, 2, 2, 3, M, M, M, M, M ]
2 [ 0, 1, 1, 2, 2, 3, M, M, M, M, M ]
5 [ 0, 1, 1, 2, 2, 1, M, M, M, M, M ] 更新なし
```

金額が満たせるものを探してより小さいもので更新していくイメージ
