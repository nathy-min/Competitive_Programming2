class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        arooms = [i for i in range(n)]
        orooms = []

        for s, e in meetings:
            while orooms and s >= orooms[0][0]:
                heappush(arooms, heappop(orooms)[1])

            if arooms:
                rnum = heappop(arooms)
            else:
                prevend, rnum   = heappop(orooms)
                e += prevend - s   
            heappush(orooms, (e, rnum))
            count[rnum] += 1

        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i           
