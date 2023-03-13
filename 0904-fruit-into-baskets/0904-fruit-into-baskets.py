class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        maxlen=0
        d={}
        while end < len(fruits):
            d[fruits[end]] = end
            if len(d)>= 3:
                minval = min(d.values())
                del d[fruits[minval]]
                start = minval+1
            maxlen = max(maxlen, end - start+1)
            end += 1
        return maxlen         