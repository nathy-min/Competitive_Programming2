class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        min_num = min(nums)
        change = (max_num - k) - (min_num + k)
        if change <= 0:
            return 0
        else:
            return change