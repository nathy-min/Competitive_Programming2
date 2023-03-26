class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        temp = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if not temp[nums[i] - 1]:
                temp[nums[i] - 1] = nums[i]
            else:
                res.append(nums[i])
        
        for i in range(len(temp)):
            if not temp[i]:
                res.append(i + 1)
                break
        
        return res