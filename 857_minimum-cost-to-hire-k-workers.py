class Solution:
    def mincostToHireWorkers(self, quality, wage, k: int) -> float:
        a = sorted([(wage[i], quality[i]) for i in range(len(quality))], key=lambda x: x[1])

        def check():
            p_group = []
            for i, (w, q) in enumerate(a):
                if w / q <= mid:
                    p_group.append(i)

            return p_group

        lo, hi = 0, max([(a[i][0] / a[i][1]) for i in range(len(a))])
        while lo < hi:
            mid = (lo + hi) / 2
            p_group = check()
            if len(p_group) < k:
                lo = mid
            if len(p_group) > k:
                hi = mid
            if len(p_group) == k:
                highest_ratio = 0
                for i in p_group:
                    highest_ratio = max(highest_ratio, a[i][0] / a[i][1])

                amount = 0
                for i in p_group:
                    amount += (a[i][1] * highest_ratio)

                return amount

        return -1


if __name__ == '__main__':
    print(Solution().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2))
    print(Solution().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3))
