class SnapshotArray:

    def __init__(self, length: int):
        self.record = [[] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.record[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        if not self.record[index]: return 0

        l, r = 0, len(self.record[index]) - 1
        idx = -1
        while l <= r:
            m = l + (r - l) // 2
            if self.record[index][m][0] <= snap_id:
                idx = max(idx, m)
                l = m + 1
            else:
                r = m - 1

        return self.record[index][idx][1] if idx != -1 else 0          


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)