class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def check(bDay):
            bouquets = 0
            counter = 0
            for t in bloomDay:
                if t <= bDay:
                    counter += 1
                else:
                    bouquets += counter // k
                    counter = 0
            return bouquets + counter // k

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid) >= m:
                hi = mid
            else:
                lo = mid + 1

        return hi if check(hi) >= m else -1


if __name__ == '__main__':
    print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
    print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
    print(Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))

