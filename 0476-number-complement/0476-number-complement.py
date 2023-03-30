class Solution:
    def findComplement(self, num: int) -> int: 
        val = int("1" * num.bit_length(), 2)
        
        return num ^ val