class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice_sub = 0
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        for pref_sum in nums:
            nice_sub += hash_map[pref_sum - k]
            hash_map[pref_sum] += 1
            
        return nice_sub    
                
                
                