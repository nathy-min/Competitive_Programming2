class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        cnt = len(ct)
        i = st = 0
        n = len(s)
        ans = n + 1
        for j in range(n):
            if s[j] in ct:
                ct[s[j]] -= 1
                if ct[s[j]] == 0:
                    cnt -= 1            
            while cnt == 0:
                if ans > j - i + 1:
                    ans = j - i + 1
                    st = i
                if s[i] in ct:
                    ct[s[i]] += 1
                    if ct[s[i]] > 0:
                        cnt += 1
                i += 1
        if ans > n:
            return ""
        return s[st:st + ans]