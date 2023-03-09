class Solution:
    def splitString(self, s: str) -> bool:
        return self.descending( s , [])

    def descending(self , ele , vtd) :
        if len(vtd) >= 2 and int(vtd[-2]) - 1 != int(vtd[-1] ):
            return False

        elif len(ele) == 0 and len(vtd) >= 2 and int(vtd[-2]) - 1 == int(vtd[-1] ) :
            return True


        for index , val in enumerate(ele) :
            vtd.append(ele[:index + 1])
            val = self.descending(ele[index + 1 :] , vtd)
            if val :
                return True
            vtd.pop()

        return False