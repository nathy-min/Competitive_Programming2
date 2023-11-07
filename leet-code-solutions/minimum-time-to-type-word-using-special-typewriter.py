class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        min_count = 0
        for ch in word:
            cur_min = abs(ord(ch) - ord(curr))
            if ch > curr:
                cur_min = min((ord('z') - ord(ch) + ord(curr) - ord('a') + 1), cur_min)
            else:
                cur_min = min((ord(ch) - ord('a') + ord('z') - ord(curr) + 1), cur_min) 
            min_count += cur_min + 1
            curr = ch

        return min_count    
                   