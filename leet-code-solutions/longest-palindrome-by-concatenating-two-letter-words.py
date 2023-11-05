class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        for key in words:
            hashmap[key] += 1

        ans = 0
        additional = 0
        temp = hashmap.copy()
        for key in temp.keys():
            if key == key[::-1]:
                
                if not hashmap[key] % 2:
                    ans += hashmap[key] * 2
                else:
                    ans += (hashmap[key] - 1) * 2
                    additional = 2    
                
                
            else:
                ans += min(hashmap[key], hashmap[key[::-1]]) * 4
                hashmap[key] = 0

        ans += additional
        return ans                    
  