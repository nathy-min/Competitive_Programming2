class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        fq = []
        fw = []
        res = []
        
        for q in queries:
            temp = sorted(list(q))
            ch = temp[0]
            fq.append(temp.count(ch))
            
        for w in words:
            temp = sorted(list(w))
            ch = temp[0]
            fw.append(temp.count(ch))    
        
        fw.sort()
        for q in fq:
            temp = 0
            left = 0
            right = len(fw) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if fw[mid] > q:
                    temp += (right - mid + 1)
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(temp)        

        return res