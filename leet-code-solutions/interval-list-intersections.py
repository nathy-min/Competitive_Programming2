class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            temp_first = max(firstList[i][0], secondList[j][0])
            temp_second = min(firstList[i][1], secondList[j][1])
            if temp_second >= temp_first:
                ans.append([temp_first, temp_second])
            if secondList[j][1] > firstList[i][1]:
                i += 1
            else:
                j += 1

        return ans                