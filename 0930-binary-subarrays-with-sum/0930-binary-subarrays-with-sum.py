class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        no_prefix = defaultdict(int)
        no_prefix[0] += 1
        no_subarry = 0
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
           
        for i in range(len(nums)):
            no_subarry += no_prefix[nums[i] - goal]
            no_prefix[nums[i]] += 1
                    
        return no_subarry        
            