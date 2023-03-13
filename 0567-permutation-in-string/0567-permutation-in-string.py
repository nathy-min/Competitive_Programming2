class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        countS2 = {}
        
        left = 0
        for right in range(len(s2)):
            countS2[s2[right]] = countS2.get(s2[right], 0) + 1
            
            if right - left + 1 == len(s1):
                if countS1 == countS2:
                    return True
                
                countS2[s2[left]] = countS2.get(s2[left], 0) - 1
                if not countS2[s2[left]]:
                    countS2.pop(s2[left])
                    
                left += 1
                
        return False
        
        print(len(countS1))