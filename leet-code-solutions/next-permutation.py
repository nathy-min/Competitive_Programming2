class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = -1
        b = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    a, b = (j, i) if j > a else (a, b)

        if a != -1:
            nums[a], nums[b] = nums[b], nums[a]
            nums[a + 1 : ] = sorted(nums[a + 1 :])           
        else:
            nums.sort()
        print(a, b)                
