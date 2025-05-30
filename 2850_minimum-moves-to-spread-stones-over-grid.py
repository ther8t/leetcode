import collections


class Solution:
    """
    This is a greedy approach to solving the problem. This doesn't work. Initially I thought it would.
    But,
    [0,2,3]
    [2,0,1]
    [0,1,0]
    Greedy ends up in a situation where index (0,2) value 3, needs to transfer to a total distance of 6(2 + 4).
    """
    def minimumMoves(self, grid: list) -> int:
        satisfied = set()
        counter = {}
        excess = set()
        unsatisfied = set()
        distances = collections.defaultdict(list)

        for r in range(3):
            for c in range(3):
                index = 3 * r + c
                if grid[r][c] == 0:
                    unsatisfied.add(index)
                elif grid[r][c] == 1:
                    satisfied.add(index)
                else:
                    excess.add(index)
                counter[index] = grid[r][c]

        def index_to_rc(index):
            return index // 3, index % 3

        def distance(a, b):
            ra, ca = index_to_rc(a)
            rb, cb = index_to_rc(b)
            return abs(rb - ra) + abs(cb - ca)

        for e in excess:
            for u in unsatisfied:
                distances[distance(e, u)].append((e, u))

        ans = 0
        for d in sorted(distances.keys()):
            for e, u in distances[d]:
                if counter[e] > 1 and counter[u] == 0:
                    counter[e] -= 1
                    counter[u] = 1
                    unsatisfied.remove(u)
                    ans += d

        return ans

    """
    Attempt #2
    Accepted : 61%
    """
    def minimumMoves(self, grid: list) -> int:
        satisfied = set()
        counter = {}
        movements = []
        excess = set()
        unsatisfied = set()

        for r in range(3):
            for c in range(3):
                index = 3 * r + c
                if grid[r][c] == 0:
                    unsatisfied.add(index)
                elif grid[r][c] == 1:
                    satisfied.add(index)
                else:
                    excess.add(index)
                counter[index] = grid[r][c]

        def index_to_rc(index):
            return index // 3, index % 3

        def distance(a, b):
            ra, ca = index_to_rc(a)
            rb, cb = index_to_rc(b)
            return abs(rb - ra) + abs(cb - ca)

        for e in excess:
            for u in unsatisfied:
                movements.append((e, u, distance(e, u)))

        def move(index, current_sum):
            nonlocal ans
            if index == len(movements):
                if len(unsatisfied) == 0:
                    ans = min(ans, current_sum)
                return
            e, u, d = movements[index]

            if counter[e] > 1 and counter[u] < 1:
                counter[e] -= 1
                counter[u] += 1
                unsatisfied.remove(u)
                move(index + 1, current_sum + d)
                counter[e] += 1
                counter[u] -= 1
                unsatisfied.add(u)

            move(index + 1, current_sum)

        ans = float('inf')
        move(0, 0)
        return int(ans)


if __name__ == '__main__':
    print(Solution().minimumMoves([[1,1,0],[1,1,1],[1,2,1]]))
    print(Solution().minimumMoves(grid = [[1,3,0],[1,0,0],[1,0,3]]))
    print(Solution().minimumMoves([[0,2,3],[2,0,1],[0,1,0]]))
