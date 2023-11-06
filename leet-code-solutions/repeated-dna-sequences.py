class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        temp = 0
        hash_set = set()
        for i in range(10):
            temp += (ord(s[i]) * pow(26, i))    
        
        hash_set.add(temp)
        ans = set()
        for i in range(10, len(s)):
            temp -= (ord(s[i - 10]))
            temp /= 26
            temp += (ord(s[i]) * pow(26, 9))
            if temp in hash_set:
                ans.add(s[i - 9 : i + 1])
            else:
                hash_set.add(temp)

        return ans           