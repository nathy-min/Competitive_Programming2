class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i,j=0,len(piles)
        a=0
        while j>i:
            i+=1
            j-=2
            a+=piles[j]
        return a