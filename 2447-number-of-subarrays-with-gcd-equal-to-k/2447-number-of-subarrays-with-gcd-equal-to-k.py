class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if not b:
                return a
            
            return gcd(b, a%b)

        count = 0
        for i in range(len(nums)):
            
            cur_gcd = 0
            for idx in range(i, len(nums)):
                cur_gcd = gcd(nums[idx], cur_gcd)
                
                if cur_gcd == k:
                    count += 1
                
                elif cur_gcd < k:
                    break
        
        return count