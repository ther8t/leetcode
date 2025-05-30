class Solution:
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        last_right, last_down = [[i for i in range(n)] for j in range(m)], [[j for i in range(n)] for j in range(m)]

        for i in range(m):
            last = n
            for j in range(n - 1, -1, -1):
                if land[i][j] == 0:
                    last = j
                else:
                    last_right[i][j] = last - 1

        for j in range(n):
            last = m
            for i in range(m - 1, -1, -1):
                if land[i][j] == 0:
                    last = i
                else:
                    last_down[i][j] = last - 1

        ans = []
        for i in range(m):
            for j in range(n):
                if (i - 1 < 0 or land[i - 1][j] == 0) and (j - 1 < 0 or land[i][j - 1] == 0) and land[i][j] == 1:
                    ans.append([i, j, last_down[i][j], last_right[i][j]])

        return ans


if __name__ == '__main__':
    print(Solution().findFarmland(land = [[1,0,0],[0,1,1],[0,1,1]]))
    print(Solution().findFarmland([[0,1],[1,0]]))
