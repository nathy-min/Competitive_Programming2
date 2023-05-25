class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n < 4:
            return 0

        ans = float("inf")
        for i in range(4):
            ans = min(ans, nums[n - i - 1] - nums[3 - i])

        return ans