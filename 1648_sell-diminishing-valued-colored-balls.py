import bisect
import heapq
import math


class Solution:
    # def maxProfit(self, inventory, orders: int) -> int:
    #     fn = lambda x: sum(max(0, xx - x) for xx in inventory)  # balls sold
    #
    #     # last true binary search
    #     lo, hi = 0, 10 ** 9
    #     while lo < hi:
    #         mid = lo + hi + 1 >> 1
    #         if fn(mid) >= orders:
    #             lo = mid
    #         else:
    #             hi = mid - 1
    #
    #     ans = 0
    #     for x in inventory:
    #         if x > lo:
    #             addition = (x + lo + 1) * (x - lo) // 2
    #             ans += addition
    #     # ans = sum((x + lo + 1) * (x - lo) // 2 for x in inventory if x > lo)
    #     return (ans - (fn(lo) - orders) * (lo + 1)) % 1_000_000_007

    def maxProfit(self, inventory, orders: int) -> int:
        MOD = (10**9 + 7)
        def search(mid):
            search_count = 0
            for i in inventory:
                if i > mid:
                    search_count += (i - mid)
            return search_count

        left, right = 0, max(inventory)
        while left < right:
            mid = (left + right) // 2 + 1
            if search(mid) >= orders:
                left = mid
            else:
                right = mid - 1

        ans = 0
        for i in inventory:
            if i > left:
                ans += (i - left) * (i + left + 1) // 2
        return (ans - (search(left) - orders) * (left + 1)) % MOD



    # # TLE : 9/95
    # def maxProfit(self, inventory, orders: int) -> int:
    #     h = []
    #     for i in inventory:
    #         heapq.heappush(h, -i)
    #
    #     ans = 0
    #     while orders:
    #         value = abs(heapq.heappop(h))
    #         top_value = abs(h[0] if h else 0)
    #         diff = max(min(orders, value - top_value), 1)
    #         ans += diff * (value - diff + 1 + value) // 2
    #         orders -= diff
    #         heapq.heappush(h, -(value - diff))
    #
    #     return abs(ans) % (10**9 + 7)

    """
    Revision 2:
    Acccepted 85%
    
    This is a difficult one and I am yet to figure out why it does what it does.
    The idea is simple enough but the problem happens when you reach adding all of them up.
    In my case, I added each inventory and the sum came out to be 373219332 whereas the answer is 373219333.
    The answer is obtained by doing the exact reverse. It adds everything beyond the height line and then deducts the orders which are not included and were added beyond the required order each of value (height + 1) 
    """
    def maxProfit(self, inventory, orders: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(inventory)
        inventory.sort()
        lo, hi = 0, max(inventory)
        inventory_sum = [0] * (n + 1)
        current_sum = 0
        for i in range(n):
            current_sum += inventory[i]
            inventory_sum[i + 1] = current_sum

        def check(height):
            index = bisect.bisect_right(inventory, height)
            return inventory_sum[n] - inventory_sum[index] - height * (n - index)

        while lo < hi:
            mid_height = (lo + hi + 1) // 2
            if check(mid_height) >= orders:
                lo = mid_height
            else:
                hi = mid_height - 1

        ans = 0
        for i in range(bisect.bisect_right(inventory, lo), n):
            ans += (inventory[i] + lo + 1) * (inventory[i] - lo) // 2
        return (ans - (check(lo) - orders) * (lo + 1)) % MOD
        # for i in range(n - 1, -1, -1):
        #     if inventory[i] < lo or orders == 0:
        #         break
        #     taken = min(inventory[i] - lo, orders)
        #     ans += taken * (inventory[i] + inventory[i] - taken + 1) // 2
        #     ans %= MOD
        #     orders -= taken
        # return ans





if __name__ == '__main__':
    print(Solution().maxProfit(inventory = [2,5], orders = 4))
    print(Solution().maxProfit(inventory = [3,5], orders = 6))
    print(Solution().maxProfit([1000000000], 1000000000))
    print(Solution().maxProfit([76], 22))
    print(Solution().maxProfit([497978859,167261111,483575207,591815159], 836556809))