import collections
import functools
import heapq


class Solution:

    """
    I misread the question at first. I read that the cells have to adjacent in order to traverse.
    This however was that we can traverse to a cell with same row or column.

    TLE
    558/566
    """
    def maxIncreasingCells(self, mat) -> int:
        r, c = len(mat), len(mat[0])
        visited = set()

        @functools.lru_cache(None)
        def search(x, y):
            score = 0
            for next_d in range(c):
                next_x, next_y = (x) % r, (y + next_d) % c
                if (next_x, next_y) not in visited and mat[next_x][next_y] - mat[x][y] > 0:
                    visited.add((next_x, next_y))
                    score = max(score, search(next_x, next_y))
                    visited.remove((next_x, next_y))

            for next_d in range(r):
                next_x, next_y = (x + next_d) % r, (y) % c
                if (next_x, next_y) not in visited and mat[next_x][next_y] - mat[x][y] > 0:
                    visited.add((next_x, next_y))
                    score = max(score, search(next_x, next_y))
                    visited.remove((next_x, next_y))

            return 1 + score

        cells = 0
        for i in range(r):
            for j in range(c):
                cells = max(cells, search(i, j))

        return cells


    """
    Surprisingly enough TLE.
    
    TLE 193/566
    SURPRISING!!!
    """
    def maxIncreasingCells(self, mat) -> int:
        r, c = len(mat), len(mat[0])
        inbound, outbound = collections.defaultdict(list), collections.defaultdict(list)

        for x in range(r):
            for y in range(c):
                for dy in range(c):
                    if mat[x][dy] - mat[x][y] > 0:
                        inbound[(x, dy)].append((x, y, x, dy))
                        outbound[(x, y)].append((x, y, x, dy))

                for dx in range(r):
                    if mat[dx][y] - mat[x][y] > 0:
                        inbound[(dx, y)].append((x, y, dx, y))
                        outbound[(x, y)].append((x, y, dx, y))

        score = [[0 for _ in range(c)] for _ in range(r)]
        def traverse(x, y, current_score):
            score[x][y] = max(score[x][y], current_score)
            for sx, sy, ex, ey in inbound[(x, y)]:
                traverse(sx, sy, current_score + 1)

        # trying to find the cells which have no outbound but have inbounds and traverse backwards and update the scores of every cell they touch.
        for i in range(r):
            for j in range(c):
                if ((i, j) not in outbound or len(outbound[(i, j)]) == 0) and (i, j) in inbound and len(inbound[(i, j)]) > 0:
                    traverse(i, j, 1)

        max_score = 1
        for i in range(r):
            for j in range(c):
                max_score = max(max_score, score[i][j])

        return max_score


    """
    TLE 193/566
    SURPRISING!!!
    """
    def maxIncreasingCells(self, mat) -> int:
        r, c = len(mat), len(mat[0])
        inbound, outbound = collections.defaultdict(list), collections.defaultdict(list)

        for x in range(r):
            for y in range(c):
                for dy in range(c):
                    if mat[x][dy] - mat[x][y] > 0:
                        inbound[(x, dy)].append((x, y, x, dy))
                        outbound[(x, y)].append((x, y, x, dy))

                for dx in range(r):
                    if mat[dx][y] - mat[x][y] > 0:
                        inbound[(dx, y)].append((x, y, dx, y))
                        outbound[(x, y)].append((x, y, dx, y))

        score = 1

        def traverse(x, y, current_score):
            if (x, y) not in outbound:
                return current_score

            score = current_score
            for sx, sy, ex, ey in outbound[(x, y)]:
                score = max(score, traverse(ex, ey, current_score + 1))

            return score

        # trying to find the cells which have no inbound but have outbounds and traverse dfs.
        for i in range(r):
            for j in range(c):
                if (i, j) in outbound and len(outbound[(i, j)]) > 0 and (i, j) not in inbound:
                    score = max(score, traverse(i, j, 1))

        return score



    def maxIncreasingCells(self, mat) -> int:
        r, c = len(mat), len(mat[0])
        value_coordinate_map = collections.defaultdict(list)

        for x in range(r):
            for y in range(c):
                value_coordinate_map[mat[x][y]].append((x, y))

        score = [[1 for _ in range(c)] for _ in range(r)]
        for k in sorted(value_coordinate_map.keys()):
            for x, y in value_coordinate_map[k]:
                for j in range(c):
                    if mat[x][j] > mat[x][y]:
                        score[x][j] = max(score[x][j], score[x][y] + 1)
                for i in range(r):
                    if mat[i][y] > mat[x][y]:
                        score[i][y] = max(score[i][y], score[x][y] + 1)

        max_score = 1
        for i in range(r):
            for j in range(c):
                max_score = max(max_score, score[i][j])

        return max_score


    """
    Memory Limit Exceeded
    """
    def maxIncreasingCells(self, mat) -> int:
        r, c = len(mat), len(mat[0])
        neighbours = collections.defaultdict(list)
        h = []

        for i in range(r):
            for j in range(c):
                for cols in range(c):
                    if mat[i][cols] > mat[i][j]:
                        neighbours[(i, j)].append((i, cols))

                for rows in range(r):
                    if mat[rows][j] > mat[i][j]:
                        neighbours[(i, j)].append((rows, j))
                h.append((mat[i][j], (i, j)))

        score = collections.defaultdict(lambda: 1)
        highest_val = 1
        for value, (i, j) in sorted(h):
            highest_val = max(highest_val, score[(i, j)])
            for ni, nj in neighbours[(i, j)]:
                if score[(ni, nj)] < score[(i, j)] + 1:
                    score[(ni, nj)] = score[(i, j)] + 1

        return highest_val


    def maxIncreasingCells(self, mat) -> int:
        r, c = len(mat), len(mat[0])
        value_coordinate_map = collections.defaultdict(list)

        for i in range(r):
            for j in range(c):
                value_coordinate_map[mat[i][j]].append((i, j))

        row_score = collections.defaultdict(int)
        col_score = collections.defaultdict(int)
        highest_score = 1
        for val in sorted(value_coordinate_map.keys()):
            temp_row = collections.defaultdict(int)
            temp_col = collections.defaultdict(int)
            for i, j in value_coordinate_map[val]:
                temp_row[i] = 1 + max(row_score[i], col_score[j])
                temp_col[j] = 1 + max(row_score[i], col_score[j])

            for i, j in value_coordinate_map[val]:
                row_score[i] = max(temp_row[i], temp_col[j], row_score[i])
                col_score[j] = max(temp_row[i], temp_col[j], col_score[j])
                highest_score = max(highest_score, row_score[i], col_score[j])

        return highest_score



if __name__ == '__main__':
    # print(Solution().maxIncreasingCells([[-1,-2]]))
    # print(Solution().maxIncreasingCells([[3,1],[3,4]]))
    # print(Solution().maxIncreasingCells(mat = [[1,1],[1,1]]))
    # print(Solution().maxIncreasingCells(mat = [[3,1,6],[-9,5,7]]))
    # print(Solution().maxIncreasingCells([[-8,4,9,-1]]))
    print(Solution().maxIncreasingCells([[-4,8,-3,2,-4,-8,7,5,-2],[-5,5,-7,-2,6,-6,-8,-4,-4]]))
