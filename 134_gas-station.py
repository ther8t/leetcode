import heapq


class Solution:

    """
    Attempt: Fired
    TLE
    """
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        h = []

        for i in range(n):
            if gas[i] >= cost[i]:
                heapq.heappush(h, (-1, i, gas[i]))

        while h:
            weight, current_index, current_fuel = heapq.heappop(h)
            if weight == -len(gas) - 1:
                return current_index

            next_pos = (current_index + 1) % n
            if current_fuel >= cost[current_index]:
                heapq.heappush(h, (weight - 1, next_pos, current_fuel - cost[current_index] + gas[next_pos]))

        return -1

    """
    Attempt: Fired
    Brute Force
    
    TLE
    """
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)

        for starting in range(n):
            next_stop = (starting + 1) % n
            if gas[starting] < cost[starting]:
                continue
            fuel = gas[starting] - cost[starting] + gas[next_stop]
            current_stop = next_stop
            while fuel >= 0 and next_stop != starting:
                next_stop = (current_stop + 1) % n
                if fuel < cost[current_stop]:
                    break
                fuel = fuel - cost[current_stop] + gas[next_stop]
                current_stop = next_stop
            if next_stop == starting and fuel >= cost[current_stop]:
                return starting

        return -1


    """
    Attempt: Fired
    Accepted: 40%
    This is a difficult one. I had figured that the solution could be around 'gains'/gas_diff. The idea was to calculate the min gas_diff can be and check if there is a place where all the fuel to the right of which including itself could be sufficient to overcome the most fuel deficit(the min gas_diff till that point).
    I guess where this logic falters is that though there can exist such a point there might also exist a lesser gas_diff further ahead which this fuel might not be sufficient to cover up.
    """
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        gas_diff = [gas[i] - cost[i] for i in range(n)]

        running_sum = 0
        total_sum = 0
        ans = 0
        for i in range(n):
            running_sum += gas_diff[i]
            total_sum += gas_diff[i]

            if running_sum <= 0:
                running_sum = 0
                ans = i + 1

        return ans % n if total_sum >= 0 else -1


    """
    Wrong Answer
    """
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        gas_diff = [gas[i] - cost[i] for i in range(n)]
        if sum(gas_diff) < 0:
            return -1

        running_sum = 0
        min_gas_diff_total = 0
        min_gas_diff = [gas_diff[i] for i in range(n)]
        for i in range(n):
            min_gas_diff[i] = min_gas_diff_total
            running_sum += gas_diff[i]
            min_gas_diff_total = min(min_gas_diff_total, running_sum)

        running_sum = 0
        for i in range(n - 1, -1, -1):
            running_sum += gas_diff[i]
            if running_sum >= abs(min_gas_diff[i]):
                return i

        return -1


if __name__ == '__main__':
    print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    print(Solution().canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
