import collections


class Solution:
    def countTriplets(self, arr) -> int:
        def getXOR(a, b):
            return running_xor[b] ^ running_xor[a - 1]

        running_xor = [0 for _ in range(len(arr) + 1)]
        xor = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            running_xor[i] = xor

        ans = 0
        for i in range(len(arr) - 1):
            for k in range(i + 1, len(arr)):
                for j in range(i + 1, k + 1):
                    if getXOR(i, j - 1) == getXOR(j, k):
                        ans += 1

        return ans

    # def countTriplets(self, arr) -> int:
    #     def getXOR(a, b):
    #         return running_xor[b] ^ running_xor[a - 1]
    #
    #     running_xor = [0 for _ in range(len(arr) + 1)]
    #     xor = 0
    #     for i in range(len(arr)):
    #         xor ^= arr[i]
    #         running_xor[i] = xor
    #
    #     m = collections.defaultdict(list)
    #     for i in range(len(arr)):
    #         for j in range(i, len(arr)):
    #             m[getXOR(i, j)].append((i, j))
    #
    #     ans = 0
    #     for c in m:
    #         for i in range(len(m[c])):
    #             for j in range(i + 1, len(m[c])):
    #                 if m[c][j][0] - m[c][i][1] == 1:
    #                     ans += 1
    #     return ans


if __name__ == '__main__':
    print(Solution().countTriplets(arr = [2,3,1,6,7]))
    print(Solution().countTriplets(arr = [1,1,1,1,1]))
