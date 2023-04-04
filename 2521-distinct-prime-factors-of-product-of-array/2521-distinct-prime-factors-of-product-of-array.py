class Solution:
    def prime_factor(self , val):
        d = 2
        while val > 1:
            if val % d == 0:
                self.sets.add(d)
                while val % d == 0:
                    val //= d
            d += 1
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.sets = set()
        for num in nums:
            self.prime_factor(num)
        return len(self.sets)