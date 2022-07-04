# DP 問題へのアプローチ

特定の問題および他のほとんどの問題は、次の順序で対処できます。

1. 再帰的関係の検索
2. 再帰 (トップダウン)
3. 再帰+メモ (トップダウン)
4. 反復+メモ (ボトムアップ)
5. 反復+N 変数 (ボトムアップ)

- 手順 1: 再帰関係を調べる。

強盗には 2 つの選択肢がある。

a) 現在の家を強奪する。

b) 現在の家を強奪するな。

オプション"a"が選択されている場合、彼女は以前の i-1 の家を奪うことはできませんが、以前の i-2 の家には安全に進めることができ、それ以降のすべての累積戦利品を得ることを意味します。

オプション"b"が選択された場合、i-1 および以下のすべての建物の盗難によって得られる可能性のあるすべての戦利品を取得します。

つまるところ何がより利益になるかを計算することになります

現在の家屋+以前の家屋からの略奪

以前の家の略奪品とそれ以前に捕らえられた略奪品

```
rob(i) = max( rob(i - 2) + currentHouseValue, rob(i - 1) )
```

- 手順 2: 再帰 (トップダウン)

```python
def rob(nums: List[int]):
    return rob(nums, nums.length - 1)

def rob(nums: List[int], i: int):
    if i < 0:
        return 0
    return max(rob(nums, i - 2) + nums[i], rob(nums, i - 1))
```

- 手順 3: 再帰+メモ (トップダウン)

```python
memo = []
def rob(nums: List[int]):
    memo = [-1] * (len(nums) + 1)
    return rob(nums, nums.length - 1)

def rob(nums: List[int], i: int):
    if i < 0:
        return 0
    if memo[i] >= 0:
        return memo[i]
    result = max(rob(nums, i - 2) + nums[i], rob(nums, i - 1))
    memo[i] = result
    return result
```

- 手順 4: 反復+メモ (ボトムアップ)

O (n) 時間で実行されるが、空間の複雑さも O (n)。再帰スタックのため、これを排除する。

```python
def rob(nums: List[int]):
    if len(nums) == 0:
        return 0
    memo = [-1] * (len(nums) + 1)
    memo[0] = 0
    memo[1] = nums[0]
    for i in range(len(nums)):
        val = nums[i]
        memo[i+1] = max(memo[i], memo[i-1] + val)

    return memo[len(nums)]
```

- 手順 5: 反復+2 変数 (ボトムアップ)

前の手順では、メモ [i] とメモ [i-1] のみを使用しているので、2 つ前の手順に戻ります。代わりに 2 つの変数で保持できます。この最適化は、フィボナッチ数列の作成や他のいくつかの問題 (リンクの貼り付け) で満たされます。

```python
def rob(nums: List[int]):
    if len(nums) == 0:
         return 0
    prev1 = 0
    prev2 = 0
    for num in nums:
        tmp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = tmp
    return prev1
```
