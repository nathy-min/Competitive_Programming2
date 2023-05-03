class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)
            heapq.heappush(stones, largest - second_largest)

        stones.append(0)
        return abs(stones[0])