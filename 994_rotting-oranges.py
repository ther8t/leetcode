class Solution:
    """
    Revision 2:
    I was able to figure out that the problem was a multipoint BFS. The only error I made was in understanding the question that  I needed to figure out the time when ALL the oranges are rotten or else return -1.
    There may be a case when a fresh orange is isolated from the rotting ones and it doesn't get rot. In which case we return -1 not minute. I thought we need to return the minute when all rotting stops.
    """
    def orangesRotting(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        orange_count, rotten_count = 0, 0
        rotten = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    orange_count += 1
                elif grid[i][j] == 2:
                    orange_count += 1
                    rotten_count += 1
                    rotten.append((0, (i, j)))

        minute = 0
        while rotten:
            m, (r, c) = rotten.pop(0)
            minute = max(minute, m)

            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    rotten.append((m + 1, (nr, nc)))
                    rotten_count += 1

        return minute if rotten_count == orange_count else -1


if __name__ == '__main__':
    print(Solution().orangesRotting(grid=[[2,1,1],[1,1,0],[0,1,1]]))
    print(Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
    print(Solution().orangesRotting(grid = [[0,2]]))
