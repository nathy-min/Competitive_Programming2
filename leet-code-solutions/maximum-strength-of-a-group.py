class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans = nums[0]
        def dfs(i, curr):
            nonlocal ans
            if i == len(nums):
                return
            temp = curr    
            curr *= nums[i]
            ans = max(ans, curr)
            dfs(i + 1, curr)
            dfs(i + 1, temp)

        dfs(0, 1)
        return int(ans)    