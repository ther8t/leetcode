class Solution:
    def minSwaps(self, data) -> int:
        n = len(data)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i] = presum[i - 1] + data[i]

        ones = presum[-2]

        min_swaps = float('inf')
        for i in range(n - ones + 1):
            min_swaps = min(min_swaps, ones - (presum[i + ones - 1] - presum[i - 1]))

        return min_swaps


if __name__ == '__main__':
    print(Solution().minSwaps(data = [1,0,1,0,1,0,0,1,1,0,1]))
    print(Solution().minSwaps(data = [0,0,0,1,0]))
    print(Solution().minSwaps(data = [1,0,1,0,1]))
