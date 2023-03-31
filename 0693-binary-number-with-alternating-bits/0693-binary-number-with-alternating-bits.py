class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if (n & 1):
            check_bit = 1
        else:
            check_bit = 0
        
        while n:
            if check_bit:
                if not (n & 1):
                    return False
                check_bit = 0
                n >>= 1
            else:
                if n & 1:
                    return False
                check_bit = 1
                n >>= 1
        
        return True