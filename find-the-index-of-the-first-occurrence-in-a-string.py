class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        i, j = 0, 1

        while j < len(needle):
            if needle[i] == needle[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]    

        i = j = 0
        print(lps)
        while j < len(haystack):
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]

            if i == len(needle):
                return j - i

        return -1