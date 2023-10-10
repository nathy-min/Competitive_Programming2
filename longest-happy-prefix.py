class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        i, j = 0, 1

        while j < len(s):
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]

        return s[0 : lps[-1]]