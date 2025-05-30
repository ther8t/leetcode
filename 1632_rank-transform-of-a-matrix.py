import collections
import heapq

from sortedcontainers import SortedList
from unionfind import unionfind


class DSU:
    def __init__(self):
        self.representative = collections.defaultdict(int)

    def find(self, a):
        if self.representative[a] != a:
            self.representative[a] = self.find(self.representative[a])
        return self.representative[a]

    def combine(self, a, b):
        if a not in self.representative: self.representative[a] = a
        if b not in self.representative: self.representative[b] = b
        self.representative[self.find(b)] = self.find(a)

    def groups(self):
        g = collections.defaultdict(set)
        for i in self.representative:
            g[self.find(i)].add(i)

        return g


class Solution:


    # TLE 37/40 : My intention with this question was to update the value of any cell which requires an increment. I start from the very low and increase the values.
    # It's easier to imagine + my idea was that it would be less costly. The lower values would either be sorted in previous iterations or they would be settled because of increment in further iterations.
    # Changing a single cell is an expensive operation because it causes a ripple effect.
    def matrixRankTransform(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        out = [[1 for _ in range(cols)] for _ in range(rows)]
        row_ranking = [[1 for _ in range(cols)] for _ in range(rows)]
        col_ranking = [[1 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            elements = set()
            sorted_row = SortedList()
            for c in range(cols):
                if matrix[r][c] not in elements:
                    elements.add(matrix[r][c])
                    sorted_row.add(matrix[r][c])
            for c in range(cols):
                row_ranking[r][c] = sorted_row.index(matrix[r][c]) + 1

        for c in range(cols):
            elements = set()
            sorted_col = SortedList()
            for r in range(rows):
                if matrix[r][c] not in elements:
                    elements.add(matrix[r][c])
                    sorted_col.add(matrix[r][c])
            for r in range(rows):
                col_ranking[r][c] = sorted_col.index(matrix[r][c]) + 1

        rank_matrix = []
        for r in range(rows):
            for c in range(cols):
                rank_matrix.append((matrix[r][c], r, c))
        rank = 0
        previous_val = -1
        for val, r, c in sorted(rank_matrix):
            if val != previous_val:
                rank += 1
                previous_val = val
            out[r][c] = max(row_ranking[r][c], col_ranking[r][c])

        queue = []
        for r in range(rows):
            for c in range(cols):
                if out[r][c] < max(row_ranking[r][c], col_ranking[r][c]):
                    queue.append((-max(row_ranking[r][c], col_ranking[r][c]), r, c, max(row_ranking[r][c], col_ranking[r][c])))

        visited = collections.defaultdict(int)
        while queue:
            h, r, c, ranking = heapq.heappop(queue)
            if out[r][c] >= ranking:
                continue

            out[r][c] = ranking

            for i in range(rows):
                if col_ranking[i][c] >= col_ranking[r][c] and ranking + col_ranking[i][c] - col_ranking[r][c] > out[i][c] and ranking + col_ranking[i][c] - col_ranking[r][c] > visited[(i, c)]:
                    visited[(i, c)] = ranking + col_ranking[i][c] - col_ranking[r][c]
                    heapq.heappush(queue, ((-(ranking + col_ranking[i][c] - col_ranking[r][c]), i, c, ranking + col_ranking[i][c] - col_ranking[r][c])))

            for i in range(cols):
                if row_ranking[r][i] >= row_ranking[r][c] and ranking + row_ranking[r][i] - row_ranking[r][c] > out[r][i] and ranking + row_ranking[r][i] - row_ranking[r][c] > visited[(r, i)]:
                    visited[(r, i)] = ranking + row_ranking[r][i] - row_ranking[r][c]
                    heapq.heappush(queue, ((-(ranking + row_ranking[r][i] - row_ranking[r][c]), r, i, ranking + row_ranking[r][i] - row_ranking[r][c])))

        return out


    # def matrixRankTransform(self, matrix):
    #     rows, cols = len(matrix), len(matrix[0])
    #     out = [[1 for _ in range(cols)] for _ in range(rows)]
    #     row_ranking = [[1 for _ in range(cols)] for _ in range(rows)]
    #     col_ranking = [[1 for _ in range(cols)] for _ in range(rows)]
    #
    #     for r in range(rows):
    #         elements = set()
    #         sorted_row = SortedList()
    #         for c in range(cols):
    #             if matrix[r][c] not in elements:
    #                 elements.add(matrix[r][c])
    #                 sorted_row.add(matrix[r][c])
    #         for c in range(cols):
    #             row_ranking[r][c] = sorted_row.index(matrix[r][c]) + 1
    #
    #     for c in range(cols):
    #         elements = set()
    #         sorted_col = SortedList()
    #         for r in range(rows):
    #             if matrix[r][c] not in elements:
    #                 elements.add(matrix[r][c])
    #                 sorted_col.add(matrix[r][c])
    #         for r in range(rows):
    #             col_ranking[r][c] = sorted_col.index(matrix[r][c]) + 1
    #
    #     rank_matrix = []
    #     for r in range(rows):
    #         for c in range(cols):
    #             rank_matrix.append((matrix[r][c], r, c))
    #     rank = 0
    #     previous_val = -1
    #     for val, r, c in sorted(rank_matrix):
    #         if val != previous_val:
    #             rank += 1
    #             previous_val = val
    #         out[r][c] = rank
    #
    #     queue = []
    #     for r in range(rows):
    #         for c in range(cols):
    #             if out[r][c] != max(row_ranking[r][c], col_ranking[r][c]):
    #                 queue.append((max(row_ranking[r][c], col_ranking[r][c]), r, c))
    #
    #     while queue:
    #         updated_ranking, r, c = queue.pop(0)
    #         if updated_ranking == out[r][c]:
    #             continue
    #
    #         for i in range(rows):
    #             tentative_value = updated_ranking + (col_ranking[i][c] - col_ranking[r][c])
    #             if col_ranking[i][c] < col_ranking[r][c] and out[i][c] >= tentative_value:
    #                 queue.append((tentative_value, r, c))
    #             elif col_ranking[i][c] == col_ranking[r][c] and out[i][c] != updated_ranking:
    #                 queue.append((tentative_value, r, c))
    #             elif col_ranking[i][c] > col_ranking[r][c] and out[i][c] <= updated_ranking:
    #                 queue.append((tentative_value, r, c))
    #
    #         for i in range(cols):
    #             tentative_value = updated_ranking + (row_ranking[r][i] - row_ranking[r][c])
    #             if row_ranking[r][i] < row_ranking[r][c] and out[r][i] >= updated_ranking:
    #                 queue.append((tentative_value, r, c))
    #             elif row_ranking[r][i] == row_ranking[r][c] and out[r][i] != updated_ranking:
    #                 queue.append((updated_ranking, r, c))
    #             elif row_ranking[r][i] > row_ranking[r][c] and out[r][i] <= updated_ranking:
    #                 queue.append((tentative_value, r, c))
    #
    #         out[r][c] = updated_ranking
    #     return out


    # """
    # TLEs : The reason is our combination of cells.
    # """
    # def matrixRankTransform(self, matrix):
    #     rows, cols = len(matrix), len(matrix[0])
    #     row_rank, col_rank = [0] * rows, [0] * cols
    #     out = [[0 for _ in range(cols)] for _ in range(rows)]
    #     dsu = DSU(rows * cols)
    #
    #     def transform_index(r, c):
    #         return cols * r + c
    #
    #     h = []
    #     similar_by_value = collections.defaultdict(list)
    #     for r in range(rows):
    #         for c in range(cols):
    #             heapq.heappush(h, (matrix[r][c], r, c))
    #             similar_by_value[matrix[r][c]].append((r, c))
    #
    #     for s in similar_by_value:
    #         arr = similar_by_value[s]
    #         for i in range(len(arr)):
    #             for j in range(i + 1, len(arr)):
    #                 if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1]:
    #                     dsu.combine(transform_index(arr[i][0], arr[i][1]), transform_index(arr[j][0], arr[j][1]))
    #
    #     similar = collections.defaultdict(set)
    #     for r in range(rows):
    #         for c in range(cols):
    #             similar[dsu.find(transform_index(r, c))].add((r, c))
    #
    #     while h:
    #         val, r, c = heapq.heappop(h)
    #         if out[r][c] != 0:
    #             continue
    #         compare_arr = [out[r][c]]
    #         for s in similar[dsu.find(transform_index(r, c))]:
    #             compare_arr.append(row_rank[s[0]])
    #             compare_arr.append(col_rank[s[1]])
    #
    #         current_rank = max(compare_arr) + 1
    #         for s in similar[dsu.find(transform_index(r, c))]:
    #             out[s[0]][s[1]] = row_rank[s[0]] = col_rank[s[1]] = current_rank
    #     return out

    """
    This was particularly difficult one to crack.
    I tried a couple of things. There was one modification which eluded me and that was to combine the row number and column number. 
    I was only thinking in terms of combining the cells but to combine the whole row and column, I did not think about.
    """
    def matrixRankTransform(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        similar_by_value = collections.defaultdict(list)
        rank = [0] * (rows + cols)
        out = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                similar_by_value[matrix[r][c]].append((r, c))

        for val in sorted(similar_by_value):
            uf = DSU()

            for r, c in similar_by_value[val]:
                uf.combine(r, c + rows)

            groups = uf.groups()
            for g in groups:
                max_rank = max([rank[i] for i in groups[g]])
                for r, c in similar_by_value[val]:
                    if uf.find(r) == uf.find(g):
                        out[r][c] = rank[r] = rank[c + rows] = max_rank + 1

        return out


if __name__ == '__main__':
    print(Solution().matrixRankTransform(matrix = [[1,2],[3,4]]))
    print(Solution().matrixRankTransform(matrix = [[7,7],[7,7]]))
    print(Solution().matrixRankTransform([[2,-11,24,15,26,-31],[-48,-49,22,37,-36,-5],[6,5,-44,27,14,-27],[36,-17,-6,13,-12,27],[46,-3,-36,31,-14,-7],[-36,27,-14,41,-40,23]]))
    print(Solution().matrixRankTransform(matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
