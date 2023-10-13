class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        r = 0
        min_ops = n
        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l] + n:
                r += 1
            temp = n - (r - l)    
            min_ops = min(min_ops, temp)

        return min_ops