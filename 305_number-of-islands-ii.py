class DSU:

    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.size = [1 for i in range(length)]

    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return parent_a
        if self.size[parent_a] > self.size[parent_b]:
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
            return parent_a
        else:
            self.parent[parent_a] = parent_b
            self.size[parent_b] += self.size[parent_a]
            return parent_b


class Solution:
    def numIslands2(self, m: int, n: int, positions):
        dsu = DSU(m * n)
        map = [[0 for _ in range(n)] for _ in range(m)]

        def coordinates_to_index(r, c):
            return r * n + c

        ans = []
        islands = set()
        for r, c in positions:
            map[r][c] = 1
            islands.add(dsu.find(coordinates_to_index(r, c)))
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and map[nr][nc] == 1:
                    for parent in [dsu.find(coordinates_to_index(nr, nc)), dsu.find(coordinates_to_index(r, c))]:
                        if parent in islands:
                            islands.remove(parent)
                    dsu.union(coordinates_to_index(r, c), coordinates_to_index(nr, nc))
                    for parent in [dsu.find(coordinates_to_index(nr, nc)), dsu.find(coordinates_to_index(r, c))]:
                        islands.add(parent)

            ans.append(len(islands))

        return ans


if __name__ == '__main__':
    print(Solution().numIslands2(m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]))
    print(Solution().numIslands2(m = 1, n = 1, positions = [[0,0]]))
    print(Solution().numIslands2(3, 3, [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]))
