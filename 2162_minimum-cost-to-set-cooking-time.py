class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        times = []

        def combine_time(minute, second):
            combined = str(minute) + ('0' + str(second))[-2:]
            ptr=0
            while ptr<len(combined) and combined[ptr] == '0':
                ptr+=1
            return combined[ptr:]

        max_minutes = targetSeconds // 60
        if max_minutes <=99:
            times.append(combine_time(max_minutes, targetSeconds % 60))

        if max_minutes > 0 and targetSeconds - 60 * (max_minutes - 1) <=99:
            times.append(combine_time(max_minutes - 1, targetSeconds - 60 * (max_minutes - 1)))

        min_cost = float('inf')
        for time in times:
            at = str(startAt)
            ptr = 0
            cost = 0
            while ptr < len(time):
                if time[ptr] != at:
                    at = time[ptr]
                    cost += moveCost
                cost += pushCost
                ptr += 1
            min_cost = min(min_cost, cost)
        return min_cost


if __name__ == '__main__':
    print(Solution().minCostSetTime(1
,9403
,9402
,6008))
