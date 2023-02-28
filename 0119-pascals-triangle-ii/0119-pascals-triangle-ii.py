class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(rowindex, ans):
            if rowindex == 0:
                return ans
            
            temp = ans.copy()
            for i in range(1,len(ans)):
                temp[i] = ans[i - 1] + ans[i]
                
            return pascal(rowindex - 1, temp)
        
        ans = [0] * (rowIndex + 1)
        ans[0] = 1
        return pascal(rowIndex, ans)
                
            