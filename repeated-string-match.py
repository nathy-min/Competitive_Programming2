class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = ceil((len(b) - 1) / len(a)) + 1
        prev_size = len(a)
        a *= n
        lps = [0] * len(a)
        i, j = 0, 1

        while j < len(b):
            if b[i] == b[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]    

        i = j = 0
        print(lps)
        while j < len(a):
            if b[i] == a[j]:
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]

            if i == len(b):
                return ceil(j / prev_size)

        return -1