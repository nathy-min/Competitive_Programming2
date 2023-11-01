class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        nums = set(arr)
        values = []
        for num in arr:
            dic[num] += 1

        for key, val in dic.items():
            values.append(val)

        values = set(values)
        return len(values) == len(nums)        
        