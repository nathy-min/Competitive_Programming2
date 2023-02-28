class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = nums.copy()
        right_prefix = nums.copy()
        prdt_arr = []
       
        for i in range(1,len(nums)):
            left_prefix[i] = (left_prefix[i] * left_prefix[i - 1])
            right_prefix[len(nums) - 1 - i] *= right_prefix[len(nums) - i]
            
        for i in range(len(nums)):
            if i == 0:
                prdt_arr.append(right_prefix[i + 1])
            elif i == len(nums) - 1:
                prdt_arr.append(left_prefix[i - 1])
            else:
                prdt_arr.append(right_prefix[i + 1] * left_prefix[i - 1])
                
        
        return prdt_arr