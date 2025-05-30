import heapq


class Solution:
    """
    Stack overflow
    """
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        moves = set()

        def move(jug1WaterContent, jug2WaterContent):
            if jug1WaterContent + jug2WaterContent == targetCapacity:
                return True

            permutations = [ # empty jug1
            (0, jug2WaterContent),

            # empty jug2
            (jug1WaterContent, 0),

            # pour jug1 into jug2
            (jug1WaterContent - min(jug1WaterContent, jug2Capacity - jug2WaterContent), jug2WaterContent + min(jug1WaterContent, jug2Capacity - jug2WaterContent)),

            # pour jug2 into jug1
            (jug1WaterContent + min(jug1Capacity - jug1WaterContent, jug2WaterContent), jug2WaterContent - min(jug1Capacity - jug1WaterContent, jug2WaterContent)),

            # fill jug1
            (jug1Capacity, jug2WaterContent),

            # fill jug2
            (jug1WaterContent, jug2Capacity)]

            for j1, j2 in permutations:
                if (j1, j2) in moves:
                    continue
                moves.add((j1, j2))
                if move(j1, j2):
                    return True

            return False

        moves.add((0, 0))
        return move(0, 0)



    """
    BFS
    Accepted 5%
    """
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        moves = set()

        s = [(0, 0)]

        while s:
            jug1WaterContent, jug2WaterContent = heapq.heappop(s)
            if jug1WaterContent + jug2WaterContent == targetCapacity:
                return True

            permutations = [ # empty jug1
            (0, jug2WaterContent),

            # empty jug2
            (jug1WaterContent, 0),

            # pour jug1 into jug2
            (jug1WaterContent - min(jug1WaterContent, jug2Capacity - jug2WaterContent), jug2WaterContent + min(jug1WaterContent, jug2Capacity - jug2WaterContent)),

            # pour jug2 into jug1
            (jug1WaterContent + min(jug1Capacity - jug1WaterContent, jug2WaterContent), jug2WaterContent - min(jug1Capacity - jug1WaterContent, jug2WaterContent)),

            # fill jug1
            (jug1Capacity, jug2WaterContent),

            # fill jug2
            (jug1WaterContent, jug2Capacity)]

            for j1, j2 in permutations:
                if (j1, j2) in moves:
                    continue
                moves.add((j1, j2))
                heapq.heappush(s, (j1, j2))

        return False


    """
    Don't ask why but if target_capacity % gcd(a, b) == 0 the target capacity can be achieved.
    """
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def gcd(num1, num2):
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)

        gcd_num = gcd(max(jug1Capacity, jug2Capacity), min(jug1Capacity, jug2Capacity))

        return jug1Capacity + jug2Capacity >= targetCapacity and bool(targetCapacity % gcd_num == 0)




if __name__ == '__main__':
    # print(Solution().canMeasureWater(jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4))
    # print(Solution().canMeasureWater(jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5))
    # print(Solution().canMeasureWater(jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3))
    # print(Solution().canMeasureWater(999911, 999913, 1))
    # print(Solution().canMeasureWater(6, 9, 1))
    print(Solution().canMeasureWater(1, 1, 12))
