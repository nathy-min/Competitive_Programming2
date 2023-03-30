class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x ^ y
        count = 0
        
        while val:
            if val & 1:
                count += 1
            val = val >> 1
        
        return count