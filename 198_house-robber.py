import functools
import heapq


class Solution:
    """
    Attempt: Fired
    Accepted: 25%
    """
    def rob(self, nums) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def robber(index):
            max_score = nums[index]
            for i in range(index + 2, n):
                max_score = max(max_score, nums[index] + robber(i))

            return max_score

        max_score = 0
        for i in range(n):
            max_score = max(max_score, robber(i))

        return max_score

    """
    Attempt: Fired
    Accepted: 20%
    """
    def rob(self, nums) -> int:
        n = len(nums)
        h = []
        heapq.heappush(h, (0, n))
        heapq.heappush(h, (0, n + 1))

        for i in range(n - 1, -1, -1):
            highest_score, h_index = heapq.heappop(h)
            shighest_score, sh_index = heapq.heappop(h)
            heapq.heappush(h, (highest_score, h_index))
            heapq.heappush(h, (shighest_score, sh_index))

            if h_index - i == 1:
                heapq.heappush(h, (-(nums[i] + (-shighest_score)), i))
                continue
            else:
                heapq.heappush(h, (-(nums[i] + (-highest_score)), i))

        score, i = heapq.heappop(h)

        return -score

    """
    Attempt: Fired
    Accepted: 20%
    """
    def rob(self, nums) -> int:
        n = len(nums)
        a = [(0, n), (0, n + 1)]

        for i in range(n - 1, -1, -1):
            if a[0][1] - i == 1:
                a.append((nums[i] + a[1][0], i))
            else:
                a.append((nums[i] + a[0][0], i))
            a = sorted(a, reverse=True)[:2]

        return a[0][0]


if __name__ == '__main__':
    print(Solution().rob(nums = [1,2,3,1]))
    print(Solution().rob(nums = [2,7,9,3,1]))

