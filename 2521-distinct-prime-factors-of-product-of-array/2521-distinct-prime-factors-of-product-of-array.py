class Solution:
    def nextPrime(self, n):
        is_prime: list[bool] = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False
        primes = []
        
        i = 2

        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1

        for val in range(len(is_prime)):
            if is_prime[val]:
                primes.append(val)
        
        return primes
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        pdt = prod(nums)
        d = 0
        prime_factors = set()
        
        primes = self.nextPrime(1000)
        print(primes)
        while d < len(primes) :
            if pdt % primes[d] == 0:
                prime_factors.add(primes[d])
                pdt //= primes[d]
            d += 1
        
        
        
        return len(prime_factors)
    
    