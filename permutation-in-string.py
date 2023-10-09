class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        i = 0
        h_s1 = h_s2 = 0
        for a in range(len(s1)):
            h_s1 += (ord(s1[a]) * ord(s1[a]))
            h_s2 += (ord(s2[a]) * ord(s2[a]))

        if h_s1 == h_s2:
            return True

        for a in range(len(s1), len(s2)):
            h_s2 -= (ord(s2[i]) * ord(s2[i]))
            h_s2 += (ord(s2[a]) * ord(s2[a]))
            if h_s2 == h_s1:
                return True
            i += 1    

        return False