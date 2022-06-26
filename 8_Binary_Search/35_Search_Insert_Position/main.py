class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return search(nums, target, 0, len(nums))

        
def search(nums: List[int], target: int, start: int, end: int) -> int:
    splited_nums = nums[start:end]
    if start == end or len(splited_nums) == 1:
        if target > nums[start]:
            return start + 1
        if target < nums[start]:
            return start - 1 if start > 0 else 0
        return start
    
    center = int(len(splited_nums)/2) + start
    if nums[center] > target:
        return search(nums, target, start, center)
    if nums[center] < target:
        return search(nums, target, center, end)
    return center