import copy


class Solution:
    # def minFlips(self, mat) -> int:
    #     hashset = {}
    #
    #     targetHash = self.hashList(mat)
    #
    #     sourceMat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    #
    #     queue = []
    #     queue.append(sourceMat)
    #     return self.search(queue, targetHash, 0, hashset)
    #
    # def hashList(self, list):
    #     hash = ""
    #     for i in range(len(list)):
    #         for j in range(len(list[0])):
    #             hash += str(list[i][j])
    #     return hash
    #
    # def search(self, queue, targetHash, level, hashset):
    #     if len(queue) == 0:
    #         return -1
    #
    #     nextSearchQueue = []
    #     for source in queue:
    #         sourceHash = self.hashList(source)
    #         if sourceHash == targetHash:
    #             return level
    #         b = source.copy()
    #         for i in range(len(source)):
    #             for j in range(len(source[0])):
    #                 flippedMat = self.flip(copy.deepcopy(source), i, j)
    #                 flippedMatHash = self.hashList(flippedMat)
    #                 if flippedMatHash not in hashset:
    #                     hashset[flippedMatHash] = level
    #                     nextSearchQueue.append(flippedMat)
    #     return self.search(nextSearchQueue, targetHash, level+1, hashset)
    #
    # def flipValueForCell(self, mat, row, col):
    #     rows, cols = len(mat), len(mat[0])
    #     if 0 <= row < rows and 0 <= col < cols:
    #         value = mat[row][col]
    #         if value == 0:
    #             mat[row][col] = 1
    #         else:
    #             mat[row][col] = 0
    #
    # def flip(self, mat, i, j):
    #     self.flipValueForCell(mat, i, j)
    #     self.flipValueForCell(mat, i - 1, j)
    #     self.flipValueForCell(mat, i + 1, j)
    #     self.flipValueForCell(mat, i, j - 1)
    #     self.flipValueForCell(mat, i, j + 1)
    #     return mat

    # METHOD 2 : This doesn't work
    #     def minFlips(self, mat) -> int:
    #         rows, cols = len(mat), len(mat[0])
    #         zeroCount, oneCount, totalCount = 0, 0, rows * cols
    #         for i in range(rows):
    #             for j in range(cols):
    #                 if mat[i][j] == 0:
    #                     zeroCount += 1
    #                 else:
    #                     oneCount += 1
    #
    #         hashset = set()
    #
    #         def hashList(list):
    #             hash = ""
    #             isPerfect = True
    #             for i in range(len(list)):
    #                 for j in range(len(list[0])):
    #                     hash += str(list[i][j])
    #                     if list[i][j] == 1:
    #                         isPerfect = False
    #             return hash, isPerfect
    #
    #         def check(row, col):
    #             if row >= 0 and row < rows and col >= 0 and col < cols:
    #                 return True if mat[row][col] == 1 else False
    #             return False
    #
    #         def crossHairCount(row, col):
    #             count = 0
    #             count += 1 if check(row, col) else 0
    #             count += 1 if check(row - 1, col) else 0
    #             count += 1 if check(row + 1, col) else 0
    #             count += 1 if check(row, col - 1) else 0
    #             count += 1 if check(row, col + 1) else 0
    #             return count
    #
    #         def minFlipCross(flipCount, row, col):
    #             def flipValueForCell(i, j):
    #                 if 0 <= i < rows and 0 <= j < cols:
    #                     value = mat[i][j]
    #                     if value == 0:
    #                         mat[i][j] = 1
    #                     else:
    #                         mat[i][j] = 0
    #
    #             def flip(i, j):
    #                 flipValueForCell(i, j)
    #                 flipValueForCell(i - 1, j)
    #                 flipValueForCell(i + 1, j)
    #                 flipValueForCell(i, j - 1)
    #                 flipValueForCell(i, j + 1)
    #             print(mat)
    #             listHash, isPerfect = hashList(mat)
    #             if isPerfect:
    #                 hashset.add(listHash)
    #                 return 0
    #             if listHash in hashset:
    #                 return -1
    #             hashset.add(listHash)
    #
    #             # find the cell which when flipped causes max ones to change
    #             maxCrossHairCount = 0
    #             matchI = 0
    #             matchJ = 0
    #             for i in range(rows):
    #                 for j in range(cols):
    #                     if i == row and j == col:
    #                         continue
    #                     count = crossHairCount(i, j)
    #                     if count > maxCrossHairCount:
    #                         maxCrossHairCount = count
    #                         matchI = i
    #                         matchJ = j
    #             print(maxCrossHairCount, matchI, matchJ)
    #             flip(matchI, matchJ)
    #             return minFlipCross(flipCount + 1, matchI, matchJ)
    #
    #         return minFlipCross(0, -1, -1)


    """
    Revision 2:
    My solution this time was a BFS with priority queue. The only concern with that is that we need to mark a configuration of array as visited for which we need to hash the array.
    Hashing the array is an O(n) operation. But what I considered for this is that we take a hash of index as bits of a number. Index 0 would be the value of 0 bit in a binary number. Thus hashing for any change becomes an O(1) operation.
    My starting point for this would have been the array itself. But the question very cleverly starts with 0 matrix. Rest all is the same.
    """

    def minFlips(self, mat) -> int:
        rows, cols = len(mat), len(mat[0])
        zeroCount, oneCount, totalCount = 0, 0, rows * cols
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
        minSteps = self.minFlipRec(0, 0, mat)
        return minSteps if minSteps != float('inf') else -1

    def checkIfZero(self, mat):
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    return False
        return True

    def minFlipRec(self, row, col, mat):
        rows, cols = len(mat), len(mat[0])

        def flipValueForCell(i, j):
            if i >= 0 and i < rows and j >= 0 and j < cols:
                value = mat[i][j]
                if value == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = 0

        def flip(i, j):
            flipValueForCell(i, j)
            flipValueForCell(i - 1, j)
            flipValueForCell(i + 1, j)
            flipValueForCell(i, j - 1)
            flipValueForCell(i, j + 1)

        if self.checkIfZero(mat):
            return 0
        flip(row, col)
        if self.checkIfZero(mat):
            return 1
        flip(row, col)

        nextCol = col + 1
        nextRow = row
        if col == cols - 1:
            nextCol = 0
            nextRow = row + 1

        notFlipSteps = float('inf')
        if nextRow < rows and nextCol < cols:
            notFlipSteps = self.minFlipRec(nextRow, nextCol, copy.deepcopy(mat))

        flip(row, col)
        flipSteps = float('inf')
        if nextRow < rows and nextCol < cols:
            flipSteps = self.minFlipRec(nextRow, nextCol, copy.deepcopy(mat))

        return min(notFlipSteps, flipSteps + 1)


if __name__ == '__main__':
    print(Solution().minFlips([[0, 0], [0, 1]]))
