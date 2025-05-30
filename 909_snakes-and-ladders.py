import collections
import heapq


class Solution:

    def snakesAndLadders(self, board) -> int:
        n = len(board)

        def b_to_c(b):
            b = b - 1
            r = b // n
            c = b % n
            if r % 2 == 1:
                c = n - 1 - c
            r = n - 1 - r
            return r, c

        target = n * n
        queue = [(0, 1)]
        visited = set()
        visited.add(1)

        while queue:
            moves, location = heapq.heappop(queue)

            for i in range(1, 7):
                if location + i <= n * n and location + i not in visited:
                    nr, nc = b_to_c(location + i)
                    if board[nr][nc] == -1:
                        if location + i == target:
                            return moves + 1
                        visited.add(location + i)
                        heapq.heappush(queue, (moves + 1, location + i))
                    else:
                        if location + i == target or board[nr][nc] == target:
                            return moves + 1
                        visited.add(location + i)
                        heapq.heappush(queue, (moves + 1, board[nr][nc]))

        return -1


if __name__ == '__main__':
    print(Solution().snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
    print(Solution().snakesAndLadders(board = [[-1,-1],[-1,3]]))
    print(Solution().snakesAndLadders([[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]))
