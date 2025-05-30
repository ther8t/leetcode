import heapq


class Solution:
    def openLock(self, deadends, target: str) -> int:
        visited = set()
        h = [(0, "0000")]
        deadends = set(deadends)

        def getNext(c, d):
            if c == "0" and d == -1:
                return "9"
            if c == "9" and d == 1:
                return "0"
            return str(int(c) + d)

        while h:
            moves, combination = heapq.heappop(h)

            if combination == target:
                return moves
            if combination in deadends:
                continue

            for p in range(4):
                for d in [-1, 1]:
                    new_combination = combination[:p] + getNext(combination[p], d) + combination[p + 1:]
                    if new_combination not in visited:
                        if new_combination == target:
                            return moves + 1
                        visited.add(new_combination)
                        heapq.heappush(h, (moves + 1, new_combination))

        return -1


if __name__ == '__main__':
    print(Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
    print(Solution().openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
    print(Solution().openLock(deadends = ["8888"], target = "0009"))
