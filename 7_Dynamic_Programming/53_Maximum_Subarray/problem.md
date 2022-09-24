# Problem

整数配列 nums を指定して、合計が最大の連続する部分配列 (少なくとも 1 つの数値を含む) を検索し、その合計を返します。

サブ配列は、配列の連続した部分です。

# 解説

```py
def maxSubArray(self, nums: List[int]) -> int:
    dp = [0] * len(nums)
    max_num = -inf

    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
        max_num = max(max_num, dp[i])

    return max_num
```

- 基本的には足したものを引き継いで行く考えは同じ
- ただ、マイナス値になったら、そこから先は見る必要なし として引き継がない

```
in: [-2,1,-3,4,-1,2,1,-5,4]

dp: [-2,0,0,0,0,0,0,0,0]

dp: [-2,1,0,0,0,0,0,0,0]

dp: [-2,1,-2,0,0,0,0,0,0]

dp: [-2,1,-2,4,0,0,0,0,0]

dp: [-2,1,-2,4,3,0,0,0,0]

dp: [-2,1,-2,4,3,5,0,0,0]

dp: [-2,1,-2,4,3,5,6,0,0]

dp: [-2,1,-2,4,3,5,6,1,0]

dp: [-2,1,-2,4,3,5,6,1,5]

```

# ref

https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
