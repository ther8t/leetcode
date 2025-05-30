class SnapshotArray:

    # # Accepted
    # def __init__(self, length: int):
    #     self.length = length
    #     self.array = {}
    #     self.snaps = []
    #     self.latestSnapID = 0
    #
    # def set(self, index: int, val: int) -> None:
    #     self.array[index] = val
    #
    # def snap(self) -> int:
    #     self.snaps.append(self.array.copy())
    #     self.latestSnapID += 1
    #     return self.latestSnapID - 1
    #
    # def get(self, index: int, snap_id: int) -> int:
    #     if index in self.snaps[snap_id]:
    #         return self.snaps[snap_id][index]
    #     return 0


    """
    Revision 2 : I got it correct. Almost. The only mistake I made was not to make a copy but it was sort of intentional and to check if maps require copy if they are used by value and not by reference.
    The other mistake I made was to erase diff and reset it after every snap. What I had missed was that value once changed for an index will remain the same.
    """
    def __init__(self, length: int):
        self.length = length
        self.diff = {}
        self.array = [0] * length
        self.snaps = {}
        self.latestSnapID = 0

    def set(self, index: int, val: int) -> None:
        self.diff[index] = val
        self.array[index] = val

    def snap(self) -> int:
        self.snaps[self.latestSnapID] = self.diff.copy()
        self.diff = {}
        self.latestSnapID += 1
        return self.latestSnapID - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snaps and index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        return self.array[index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

if __name__ == '__main__':
    s = SnapshotArray(1)
    s.set(0, 5)
    print(s.snap())
    s.set(0, 6)
    print(s.get(0, 0))
    print(s.snap())
    print(s.snap())
    s.set(0, 12)
    print(s.get(0, 1))
    print(s.snap())
    print(s.get(0, 3))
