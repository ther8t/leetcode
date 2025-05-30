class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        def trips_for_time(current_time):
            current_total_trips = 0
            for t in time:
                current_total_trips += current_time // t
            return current_total_trips

        lo, hi = 0, 10**2

        while lo < hi:
            mid = (lo + hi) // 2
            mid_trips = trips_for_time(mid)
            if mid_trips < totalTrips:
                lo = mid + 1
            else:
                hi = mid

        return hi


if __name__ == '__main__':
    # print(Solution().minimumTime(time = [1,2,3,4], totalTrips = 5))
    # print(Solution().minimumTime(time = [2], totalTrips = 1))
    print(Solution().minimumTime([5,10,10], 9))

