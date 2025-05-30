class Solution:
    """
    Revision 2:
    A much simplified version of the solution.
    """
    def removeOnes(self, grid) -> bool:
        rows, cols = len(grid), len(grid[0])

        def flipped(row):
            ans = []
            for c in range(cols):
                ans.append(1 if grid[row][c] == 0 else 0)
            return ans

        for r in range(1, rows):
            if grid[r] != grid[0] and flipped(r) != grid[0]:
                return False

        return True




    # def removeOnes(self, grid) -> bool:
    #     if len(grid) == 1:
    #         return True
    #     for i in range(len(grid) - 1):
    #         for j in range(i+1, len(grid)):
    #             if grid[i] != grid[j] and grid[i] != self.flip(grid[j]):
    #                 return False
    #
    #     return True

    # def removeOnes(self, grid) -> bool:
    #     if len(grid) == 1:
    #         return True
    #
    #     for i in range(len(grid) - 1):
    #         zeros = 0
    #         ones = 0
    #         for j in range(len(grid[0]) - 1):
    #             if grid[i][j] == 0:
    #                 zeros+=1
    #             else:
    #                 ones+=1
    #             if grid[i][j+1] == 0:
    #                 zeros+=1
    #             else:
    #                 ones+=1
    #             if grid[i+1][j] == 0:
    #                 zeros+=1
    #             else:
    #                 ones+=1
    #             if grid[i+1][j+1] == 0:
    #                 zeros+=1
    #             else:
    #                 ones+=1
    #
    #             if zeros == 3 or ones == 3:
    #                 return False
    #
    #     return True

    def flip(self, row):
        for i in range(len(row)):
            if row[i] == 1:
                row[i] = 0
                continue
            if row[i] == 0:
                row[i] = 1
                continue
        return row

if __name__ == '__main__':
    print(Solution().removeOnes([[1,1,1],[0,0,0],[1,1,1]]))
    print(Solution().removeOnes(grid = [[0,1,0],[1,0,1],[0,1,0]]))
    print(Solution().removeOnes(grid = [[1,1,0],[0,0,0],[0,0,0]]))
    print(Solution().removeOnes(grid = [[0]]))
    print(Solution().removeOnes([[1,0,1,0],[0,0,0,0],[0,1,0,1],[1,1,1,1]]))

