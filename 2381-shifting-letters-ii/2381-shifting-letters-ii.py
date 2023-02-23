class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        zeros = [0] * len(s)
        for start, end, val in shifts:
            if val == 0:
                val = -1
            zeros[start] += val
            if end < len(s) - 1:
                zeros[end + 1] += (-1 * val)
        for i in range(1, len(zeros)):
            zeros[i] += zeros[i - 1]
            
        ans = ''
        for i in range(len(s)):
            asci_val = ord(s[i]) - ord('a')
            val = (asci_val + zeros[i]) % 26 + ord('a')
            ans += chr(val)
            
        return ans    