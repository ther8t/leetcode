from sortedcontainers import SortedList


class SORTracker:
    def __init__(self):
        self.tracker = SortedList()
        self.query_count = 0

    def add(self, name: str, score: int) -> None:
        self.tracker.add((-score, name))

    def get(self) -> str:
        ans = self.tracker[self.query_count][1]
        self.query_count += 1
        return ans


if __name__ == '__main__':
    # Your SORTracker object will be instantiated and called as such:
    obj = SORTracker()
    obj.add("bradford", 2)
    obj.add("branford", 3)
    print(obj.get())
    obj.add("alps", 2)
    print(obj.get())
    obj.add("orland", 2)
    print(obj.get())
    obj.add("orlando", 3)
    print(obj.get())
    obj.add("alpine", 2)
    print(obj.get())
    print(obj.get())
