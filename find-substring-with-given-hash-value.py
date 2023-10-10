class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        p = power
        m = modulo
        n = len(s)
        pow_dic = {}
        for i in range(k):
            pow_dic[i] = pow(p, i, m)

        temp = 0
        first = 0
        s = s[::-1]
        ans = ''
        for i in range(n):
            if i == k - 1:
                temp = (temp * p) % m
                temp = (temp + ((ord(s[i]) - 96) % m)) % m
                if hashValue == temp:
                    ans = s[first: i + 1]
            elif i >= k:
                remove = (((ord(s[first]) - 96) % m) * pow_dic[k - 1]) % m
                temp = (temp - remove + m) % m
                temp = (temp * p) % m
                temp = (temp + ((ord(s[i]) - 96) % m)) % m 
                first += 1
                
                if hashValue == temp:
                    ans = s[first : i + 1]
            else:
                temp = (temp * p) % m
                temp = (temp + ((ord(s[i]) - 96) % m)) % m


        return ans[::-1]