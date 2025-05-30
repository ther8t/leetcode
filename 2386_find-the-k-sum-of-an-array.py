from heapq import heappush, heappop


class Solution:
    # Not my solution. It is tougher than I wanted to spend my time on.
    def kSum(self, nums, k: int) -> int:
        m = sum(x for x in nums if x > 0)
        pq = [(-m, 0)]
        vals = sorted(abs(x) for x in nums)
        for _ in range(k):
            x, i = heappop(pq)
            if i < len(vals):
                heappush(pq, (x+vals[i], i+1))
                if i: heappush(pq, (x-vals[i-1]+vals[i], i+1))
        return -x


if __name__ == '__main__':
    print(Solution().kSum([-2, 1, 2, 4], 5))
