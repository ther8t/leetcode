import collections
import functools


class Solution:

    # TLE : Please understand this very well. This TLEs for a very good reason. There can be 10^5 tires. There can only by max 16 such laps that a tire can run without changing.
    # Even though a loop of theirs should be an mxn kind. But there is a huge difference between both mxn and nxm.
    # The key is exit. A tire which cannot go further without change exits the loop. However like in this case if I conduct a loop with laps outside, the loop doesn't exit.
    def minimumFinishTime(self, tires, changeTime: int, numLaps: int) -> int:
        dp = [float('inf')] * (numLaps + 1)
        dp[1] = min(tires, key=lambda x:x[0])[0]

        for t in tires:
            current_time = t[0]
            cumulated_time = t[0]
            for lap in range(1, min(16, numLaps) + 1):
                dp[lap] = min(dp[lap], cumulated_time)
                if current_time * t[1] <= t[0] + changeTime:
                    current_time *= t[1]
                    cumulated_time += current_time
                else:
                    break

        for lap in range(2, numLaps + 1):
            for i in range(1, lap // 2 + 1):
                dp[lap] = min(dp[lap], dp[i] + changeTime + dp[lap - i])

        return dp[numLaps]


    # """
    # After a lot of effort and iterations, I figured it out.
    # There were a lot of deductions to be done before calculating the actual answer.
    # The only thing which I failed to deduce was that I could dp nit just to the maximum lap which can be done without tire change, but till the very last lap.
    # This solution however TLEs.
    # """
    # def minimumFinishTime(self, tires, changeTime: int, numLaps: int) -> int:
    #     # check till when is a tyre good for. The time of the next lap should be less than changing time, else it's a bad choice to keep this tyre.
    #     tyre_time_map = collections.defaultdict(int)
    #     max_laps_single_tyre = 0
    #     for index, (f, r) in enumerate(tires):
    #         current_time = f
    #         cumulated_time = f
    #         lap = 1
    #         while current_time <= changeTime + f:
    #             tyre_time_map[(index, lap)] = cumulated_time
    #             max_laps_single_tyre = max(max_laps_single_tyre, lap)
    #             current_time *= r
    #             cumulated_time += current_time
    #             lap += 1
    #
    #     most_sensible_tyre_for_lap = collections.defaultdict(int)
    #     for lap in range(1, max_laps_single_tyre + 1):
    #         most_sensible_tyre_for_lap[lap] = (float('inf'), -1)
    #         for t in range(len(tires)):
    #             if (t, lap) in tyre_time_map and tyre_time_map[(t, lap)] < most_sensible_tyre_for_lap[lap][0]:
    #                 most_sensible_tyre_for_lap[lap] = (tyre_time_map[(t, lap)], t)
    #
    #     # @lru_cache(None)
    #     # def dfs(remaining_laps, time):
    #     #     if remaining_laps == 0:
    #     #         return time
    #     #     min_time = float('inf')
    #     #     for lap in range(1, min(remaining_laps, max_laps_single_tyre) + 1):
    #     #         laps_time, tyre = most_sensible_tyre_for_lap[lap]
    #     #         min_time = min(min_time, dfs(remaining_laps - lap, time + laps_time + changeTime))
    #     #     return min_time
    #     #
    #     # return dfs(numLaps, 0) - changeTime
    #
    #     dp = collections.defaultdict(int)
    #     dp[1] = most_sensible_tyre_for_lap[1][0]
    #     for i in range(2, numLaps + 1):
    #         dp[i] = most_sensible_tyre_for_lap[i][0] if i in most_sensible_tyre_for_lap else float('inf')
    #         for j in range(1, i):
    #             dp[i] = min(dp[i], dp[j] + changeTime + dp[i - j])
    #
    #     return dp[numLaps]



    # # TLE : No wonder this causes TLE. Perhaps not because of the number of iterations but because of the shear large computation required.
    # def minimumFinishTime(self, tires, changeTime: int, numLaps: int) -> int:
    #
    #     @lru_cache(None)
    #     def dfs(tire_index, laps_completed_on_this_tire, time, laps_completed):
    #         if laps_completed == numLaps:
    #             return time
    #
    #         # same tyre
    #         min_time = dfs(tire_index, laps_completed_on_this_tire + 1, time + tires[tire_index][0] * pow(tires[tire_index][1], laps_completed_on_this_tire), laps_completed + 1)
    #
    #         # change tyre
    #         if laps_completed_on_this_tire != 0:
    #             for i in range(len(tires)):
    #                 min_time = min(min_time, dfs(i, 0, time + changeTime, laps_completed))
    #
    #         return min_time
    #
    #     min_time = float('inf')
    #     for i in range(len(tires)):
    #         min_time = min(min_time, dfs(i, 0, 0, 0))
    #     return min_time


    def minimumFinishTime(self, tires, changeTime: int, numLaps: int) -> int:
        @functools.lru_cache(None)
        def dfs(starting_tyre, laps_left):
            if laps_left == 0:
                return 0
            min_time = float('inf')
            current_time = 0
            for l in range(1, laps_left + 1):
                current_lap_time = tires[starting_tyre][0] * (tires[starting_tyre][1] ** (l - 1))
                current_time += current_lap_time
                for n in range(len(tires)):
                    if current_lap_time > changeTime + tires[starting_tyre][0] * tires[starting_tyre][1]:
                        break
                    min_time = min(min_time, current_time + changeTime + dfs(n, laps_left - l))

            return min(min_time, current_time)

        min_time = float('inf')
        for i in range(len(tires)):
            min_time = min(min_time, dfs(i, numLaps))

        return min_time

    def minimumFinishTime(self, tires, changeTime: int, numLaps: int) -> int:
        @functools.lru_cache(None)
        def dfs(laps_left):
            if laps_left <= 0:
                return 0
            min_time = float('inf')
            for t in tires:
                current_time = t[0]
                cummulated_time = t[0]
                for l in range(1, laps_left + 1):
                    if current_time <= t[0] + changeTime:
                        min_time = min(min_time, dfs(laps_left - l) + cummulated_time + changeTime)
                        current_time *= t[1]
                        cummulated_time += current_time
            return min_time

        return dfs(numLaps) - changeTime


if __name__ == '__main__':
    print(Solution().minimumFinishTime(tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4))
    print(Solution().minimumFinishTime(tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5))
    print(Solution().minimumFinishTime([[2,2]], 21, 4))
    print(Solution().minimumFinishTime([[1,2]], 1, 1))
    print(Solution().minimumFinishTime([[99,7]], 85, 95))
    print(Solution().minimumFinishTime([[45,23],[404,3],[735,24],[856,3],[249,11],[326,7],[589,8],[91,17],[126,24],[713,21],[606,13],[585,5],[861,30],[604,4],[822,27],[231,6],[507,6],[265,5],[912,12],[878,29],[46,6],[421,20],[941,26],[151,25],[490,4],[315,14],[630,16],[292,24],[214,2],[432,18],[520,21],[88,26],[4,21],[337,28],[780,9],[220,29],[721,13],[927,25],[67,25],[835,21],[646,19],[973,26],[235,12],[427,9],[471,21],[267,16],[388,8],[788,13],[937,27],[810,26],[288,5],[966,28],[698,15],[343,12],[648,20],[238,4],[436,15],[588,4],[373,15],[100,12],[180,19],[904,15],[854,21],[107,2],[822,12],[485,24],[196,10],[978,24],[178,10],[642,29],[455,16],[490,17],[455,25],[77,7],[456,15],[102,25],[767,19],[169,5],[461,11],[385,25],[896,5],[185,26],[885,14],[948,26],[907,6],[877,18],[421,24],[783,15],[999,20],[756,10],[308,12],[34,12],[339,17],[613,15],[270,10],[681,3],[385,15],[123,4],[10,20],[799,28],[506,23],[265,24],[193,4],[638,23],[144,29],[874,19],[470,14],[195,16],[77,23],[573,28],[559,12],[146,10],[538,10],[705,4],[592,26],[258,24],[900,25],[836,8],[353,5],[197,26],[572,21],[347,17],[763,21],[67,20],[927,6],[135,4],[392,30],[131,15],[650,23],[100,30],[848,9],[858,27],[203,15],[249,4],[884,15],[465,18],[316,30],[730,15],[310,19],[823,21],[785,21],[15,16]], 772, 502))
    print(Solution().minimumFinishTime([[36,5],[32,5],[88,8],[11,4],[52,2],[2,2],[90,5],[49,6],[68,9],[77,3],[42,7],[17,3],[73,7],[89,2],[92,9],[40,7],[71,8],[79,3],[55,6],[77,9],[14,3],[87,10],[4,2],[63,7],[79,8],[3,9],[44,2],[49,9],[91,3],[58,6],[62,3],[72,7],[97,6],[29,5],[88,9],[40,8],[36,4],[82,8],[53,8],[26,2],[26,6],[92,2],[46,2],[75,6],[85,2],[6,10],[12,4],[15,4]], 24, 27))

