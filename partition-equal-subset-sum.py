class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        
        target = total_sum // 2
        @cache
        def dp(ptr, curr_sum):
            if ptr == len(nums):
                return False
            if curr_sum == target:
                return True

            return (dp(ptr + 1, curr_sum + nums[ptr]) or dp(ptr + 1, curr_sum))

        return dp(0, 0)