class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        for i in range(ord('A'), ord('Z')+1):
            
            left = 0
            operations = k
            target = chr(i)
            
            for right in range(len(s)):
                
                if s[right] != target:
                    operations -= 1
                    
                while operations < 0:
                    if s[left] != target:
                         operations += 1
                        
                    left+=1
                    
                max_length = max(max_length, right - left + 1)
                
        return max_length