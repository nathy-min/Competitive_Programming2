class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        
        return self.gcd(a, b)