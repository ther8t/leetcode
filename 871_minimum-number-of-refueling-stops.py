import functools
import heapq


class Solution:
    """
    This is a greedy solution. And I must say, this was not easy to comprehend. It checks for the most fuel from a station, not the most range.
    Assume you run out of fuel at after 4 station. Which station would you rather have filled the tank at? The one which would have gotten you the most fuel, thus most range.
    The thing to think about in this question and the reason why greedy approach works is that there cannot be a station selling less fuel which would increase the range more than the one selling more fuel.
    """
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        current_position, current_range = 0, startFuel
        last_fuel_stop = -1
        pq = []
        stops = 0

        while current_range < target:
            while last_fuel_stop + 1 < len(stations) and stations[last_fuel_stop + 1][0] <= current_range:
                heapq.heappush(pq, -stations[last_fuel_stop + 1][1])
                last_fuel_stop += 1
            if not pq:
                return -1
            next_fuel = -heapq.heappop(pq)
            current_position = current_range
            current_range = current_position + next_fuel
            stops += 1

        return stops

    # """
    # Revise this question for the second method. I don't have enough time to think about it. I have to move on.
    # """
    # def minRefuelStops(self, target: int, startFuel: int, stations) -> int:



    # # Wrong Answer : My approach was to pick the station which gives me the longest range, starting from my position.
    # # This doesn't work.
    # def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
    #
    #     def dfs(position, fuel, stops, last_fuel_stop_index):
    #         if position + fuel >= target:
    #             return stops
    #
    #         max_next_range = -1
    #         next_position, next_fuel, next_stops, next_fuel_stop_index = position, fuel, stops, last_fuel_stop_index
    #         for i in range(last_fuel_stop_index + 1, len(stations)):
    #             remaining_fuel = fuel - (stations[i][0] - position)
    #             next_range = remaining_fuel + stations[i][1]
    #             if next_range >= target:
    #                 return stops + 1
    #             if remaining_fuel < 0:
    #                 break
    #             if next_range >= max_next_range:
    #                 max_next_range = next_range
    #                 next_position, next_fuel, next_stops, next_fuel_stop_index = stations[i][0], remaining_fuel + stations[i][1], stops + 1, i
    #         if max_next_range == -1:
    #             return -1
    #         return dfs(next_position, next_fuel, next_stops, next_fuel_stop_index)
    #
    #     return dfs(0, startFuel, 0, -1)


    # # TLE DFS solution to the problem with minimum. Could also be done with binary search.
    # def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
    #     min_stops = float('inf')
    #
    #     @functools.lru_cache(None)
    #     def dfs(position, fuel, stops, last_fuel_stop_index):
    #         nonlocal min_stops
    #         if stops > min_stops:
    #             return
    #         if position + fuel >= target:
    #             min_stops = min(min_stops, stops)
    #             return
    #
    #         for i in range(last_fuel_stop_index + 1, len(stations)):
    #             remaining_fuel = fuel - (stations[i][0] - position)
    #             if remaining_fuel >= target - position:
    #                 min_stops = min(min_stops, stops + 1)
    #                 return
    #             if remaining_fuel < 0:
    #                 break
    #             dfs(stations[i][0], remaining_fuel + stations[i][1], stops + 1, i)
    #
    #     dfs(0, startFuel, 0, -1)
    #     return -1 if min_stops == float('inf') else min_stops

    # # TLE Dijikstra solution to the problem.
    # def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
    #     stations.sort()
    #     queue = []
    #     visited = set()
    #     # number of stops, position, fuel
    #     visited.add((0, 0, startFuel))
    #     heapq.heappush(queue, (0, target, 0, startFuel, -1))
    #
    #     while queue:
    #         stops, distance_left, position, fuel, last_filled_station_index = heapq.heappop(queue)
    #         if position + fuel >= target:
    #             return stops
    #
    #         for i in range(last_filled_station_index + 1, len(stations)):
    #             if stations[i][0] - position > fuel:
    #                 break
    #             remaining_fuel = fuel - (stations[i][0] - position)
    #             if (stops + 1, stations[i][0], fuel + stations[i][1]) not in visited:
    #                 if remaining_fuel + stations[i][1] >= target:
    #                     return stops + 1
    #                 heapq.heappush(queue, (stops + 1, target - stations[i][0], stations[i][0], remaining_fuel + stations[i][1], i))
    #                 visited.add((stops + 1, target - stations[i][0], stations[i][0], remaining_fuel + stations[i][1]))
    #
    #     return -1

    """
    Attempt: Fired
    Accepted
    
    The idea for this question is brilliant. This question is similar to 45_jump-game-ii, but..
    There is a slight difference. Here we are not bound to make a jump from whatever station we are on, we can store as much fuel as we want to,
    so we can chose the stations we want to stop at.
    The difference is that we can chose just one jump from the previous heap in the case of jump game and that to between the previous jump and now.
    But in the case of this question we can chose multiple station we want to fill at.
    The test case was stuck because I implemented the same algo as jump game. It could not even reach the station.
    Let's say there were stations with fuel ...34, 35.... Jump game would consider 35 because that gives the farthest jump. Sure that's right, but that does not stop us from fueling at 34.
    There was a case when we needed both.    
    """
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        fuel_stops = 0
        farthest = startFuel
        fuel_station_choices = []
        stations.append([target, 0])
        for distance, fuel in stations:
            while fuel_station_choices and distance > farthest:
                next_fuel = heapq.heappop(fuel_station_choices)
                farthest += -next_fuel
                fuel_stops += 1
            if distance > farthest:
                return -1

            heapq.heappush(fuel_station_choices, -fuel)

        return fuel_stops




if __name__ == '__main__':
    print(Solution().minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
    print(Solution().minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))
    print(Solution().minRefuelStops(target = 1, startFuel = 1, stations = []))
    print(Solution().minRefuelStops(1000, 36, [[7,13],[10,11],[12,31],[22,14],[32,26],[38,16],[50,8],[54,13],[75,4],[85,2],[88,35],[90,9],[96,35],[103,16],[115,33],[121,6],[123,1],[138,2],[139,34],[145,30],[149,14],[160,21],[167,14],[188,7],[196,27],[248,4],[256,35],[262,16],[264,12],[283,23],[297,15],[307,25],[311,35],[316,6],[345,30],[348,2],[354,21],[360,10],[362,28],[363,29],[367,7],[370,13],[402,6],[410,32],[447,20],[453,13],[454,27],[468,1],[470,8],[471,11],[474,34],[486,13],[490,16],[495,10],[527,9],[533,14],[553,36],[554,23],[605,5],[630,17],[635,30],[640,31],[646,9],[647,12],[659,5],[664,34],[667,35],[676,6],[690,19],[709,10],[721,28],[734,2],[742,6],[772,22],[777,32],[778,36],[794,7],[812,24],[813,33],[815,14],[816,21],[824,17],[826,3],[838,14],[840,8],[853,29],[863,18],[867,1],[881,27],[886,27],[894,26],[917,3],[953,6],[956,3],[957,28],[962,33],[967,35],[972,34],[984,8],[987,12]]))
