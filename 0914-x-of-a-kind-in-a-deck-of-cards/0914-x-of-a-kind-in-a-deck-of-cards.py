class Solution:
    def gcd(self, a, b):
        if not b:
            if a > 1:
                return True
            else:
                return False
        return self.gcd(b, a % b)    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        max_number = max(deck) + 1
        partition = defaultdict(int)
        if len(deck) == 1:
            return False
        for val in deck:
            partition[val] += 1
        
        cur_val = partition[deck[0]]
        
        for i in range(1,len(deck)):
            if not self.gcd(partition[deck[i]] , partition[deck[i - 1]]):
                return False
        return True    
            
        