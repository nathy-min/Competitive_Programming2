class Solution:
    def findComplement(self, num: int) -> int: 
        no_bit = 0
        temp = num
        while temp != 0:
            no_bit += 1
            temp = temp >> 1
            
        val = int("1" * no_bit, 2)
        return num ^ val