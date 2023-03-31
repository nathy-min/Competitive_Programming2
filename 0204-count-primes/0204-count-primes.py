class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n)]
        if n > 0:
            is_prime[0] = False
        if n > 1:
            is_prime[1] = False
        
        i = 2
        
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
                
            i += 1
        
        count = 0
        for val in is_prime:
            if val:
                count += 1
        
        return count