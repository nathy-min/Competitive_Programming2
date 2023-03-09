class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ele = []
        self.n = n
        self.k = k
        canidates = [ i for i in range(1 , n + 1) ]

        self.comb_search( [ ] , canidates)
        return self.ele


    def comb_search(self , vtd , loc ):
        if self.k == len(vtd) :
            new = vtd.copy()
            self.ele.append(new)
            return True
        length = len(loc)
        for index , can in enumerate(loc):
            vtd.append(can)
            val = self.comb_search(vtd , loc[index + 1:])
            vtd.remove(can)