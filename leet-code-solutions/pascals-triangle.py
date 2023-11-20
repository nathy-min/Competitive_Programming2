class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]    

        ans = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            curr = [1]
            for a in range(1, i - 1):
                curr.append(ans[-1][a - 1] + ans[-1][a])
            curr.append(1)
            ans.append(curr)

        return ans            