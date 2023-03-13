class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        j = 0
        res = float("inf")
        

        for i in range(0, len(nums)):
            total+=nums[i]
            while total >= target  and j < len(nums):
                total -= nums[j]
                res=min(res,i-j+1)
                j+=1
        if res ==  float("inf"):
            return 0
        return res