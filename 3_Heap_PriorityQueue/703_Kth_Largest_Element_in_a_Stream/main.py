from heapq import heapify, heappop, heappush, heappushpop
from typing import List

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        # Keep popping smaller elemnts till size = k
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)
        return self.nums[0]
