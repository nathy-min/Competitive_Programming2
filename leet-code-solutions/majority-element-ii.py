class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        count1 = count2 = 0     
        
        candidate1 = candidate2 = 0

        
        for num in nums:
           
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num

            
            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num
            
           
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

            
            else:
                count1 -= 1
                count2 -= 1

        result = []
        threshold = len(nums) // 3  

       
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result