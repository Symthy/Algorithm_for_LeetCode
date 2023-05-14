# Problem

整数配列 nums を指定すると、最長の厳密に増加するサブシーケンスの長さを返します。

## 解説

サブシーケンスは、残りの要素の順序を変更せずに、一部の要素を削除するか、または要素を削除しないことによって、配列から派生できるシーケンスです。たとえば、[0、3、6、7]は、配列[0, 3, 1, 6, 2, 2, 7]のサブシーケンスです。

```python
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
```

```
[0, 3, 1, 6, 2, 2, 7]

dp:
[1, 1, 1, 1, 1, 1, 1]

i=0,j=0: loopしない
i=1,j=0:
    nums[i] > nums[j]: 3 > 0
    dp[i] < dp[j] + 1: 1 < 2
    [1, 2, 1, 1, 1, 1, 1]
i=2,j=0:
    nums[i] > nums[j]: 1 > 0
    dp[i] < dp[j] + 1: 1 < 2
    [1, 2, 2, 1, 1, 1, 1]
i=2,j=1:
    nums[i] > nums[j]: 1 > 3
i=3,j=0:
    nums[i] > nums[j]: 6 > 0
    dp[i] < dp[j] + 1: 1 < 2
    [1, 2, 2, 2, 1, 1, 1]
i=3,j=1:
    nums[i] > nums[j]: 6 > 3
    dp[i] < dp[j] + 1: 2 < 3
    [1, 2, 2, 3, 1, 1, 1]
i=3,j=2:
    nums[i] > nums[j]: 6 > 1
    dp[i] < dp[j] + 1: 3 < 3
i=4,j=0:
    nums[i] > nums[j]: 2 > 0
    dp[i] < dp[j] + 1: 1 < 2
    [1, 2, 2, 3, 2, 1, 1]
i=4,j=1:
    nums[i] > nums[j]: 2 > 3
    [1, 2, 2, 3, 2, 1, 1]
i=4,j=2:
    nums[i] > nums[j]: 2 > 1
    dp[i] < dp[j] + 1: 2 < 2+1(3)
    [1, 2, 2, 3, 3, 1, 1]
i=4,j=3:
    nums[i] > nums[j]: 2 > 6
    [1, 2, 2, 3, 3, 1, 1]
i=5,j=0:
    nums[i] > nums[j]: 2 > 0
    dp[i] < dp[j] + 1: 1 < 1+1(2)
    [1, 2, 2, 3, 3, 2, 1]
i=5,j=1:
    nums[i] > nums[j]: 2 > 3
    [1, 2, 2, 3, 3, 2, 1]
i=5,j=2:
    nums[i] > nums[j]: 2 > 1
    dp[i] < dp[j] + 1: 2 < 2+1
    [1, 2, 2, 3, 3, 3, 1]
i=5,j=3:
    nums[i] > nums[j]: 2 > 6
    [1, 2, 2, 3, 3, 3, 1]
i=5,j=4:
    nums[i] > nums[j]: 2 > 2
    [1, 2, 2, 3, 3, 3, 1]
i=6,j=0:
    nums[i] > nums[j]: 7 > 0
    dp[i] < dp[j] + 1: 1 < 1+1
    [1, 2, 2, 3, 3, 3, 2]
i=6,j=1:
    nums[i] > nums[j]: 7 > 3
    dp[i] < dp[j] + 1: 2 < 2+1
    [1, 2, 2, 3, 3, 3, 3]
i=6,j=2:
    nums[i] > nums[j]: 7 > 1
    dp[i] < dp[j] + 1: 3 < 2+1
    [1, 2, 2, 3, 3, 3, 3]
i=6,j=3:
    nums[i] > nums[j]: 7 > 6
    dp[i] < dp[j] + 1: 3 < 3+1
    [1, 2, 2, 3, 3, 3, 4]
i=6,j=4:
    nums[i] > nums[j]: 7 > 2
    dp[i] < dp[j] + 1: 4 < 3+1
    [1, 2, 2, 3, 3, 3, 4]
i=6,j=5:
    nums[i] > nums[j]: 7 > 2
    dp[i] < dp[j] + 1: 4 < 3+1
    [1, 2, 2, 3, 3, 3, 4]
```

0-3-6-7

nums = [0, 3, 1, 6, 2, 2, 7]
