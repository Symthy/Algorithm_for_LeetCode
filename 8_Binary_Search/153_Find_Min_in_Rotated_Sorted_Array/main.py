# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/3293658/python-binary-search-mind-blowing-logic/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = nums[0]
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break
            mid = (low + high) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return res
