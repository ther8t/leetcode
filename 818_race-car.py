import collections
import heapq


class Solution:
    def racecar(self, target: int) -> int:
        s = [pow(2, _) for _ in range(0, 14)]

        def raceCarMove(target, at, speed):
            if at == target:
                return 0
            if abs(target - at) > target:
                return float('inf')
            moveAheadSteps = raceCarMove(target, at + speed, speed * 2)
            moveReverseSteps = raceCarMove(target, at, -1 * (speed // abs(speed)))
            return (moveAheadSteps + 1) if len(moveAheadSteps) < len(moveReverseSteps) else (
                    moveReverseSteps + 1)

        return raceCarMove(target, 0, 1)

    # def racecar(self, target: int) -> int:
    #     at = 0
    #     speed = 1
    #
    #     string = ""
    #
    #     while at != target:
    #         projectedAt = at + speed
    #         if abs(target - at) <= abs(projectedAt - target):
    #             string += "R"
    #             speed = -1 * (speed // abs(speed))
    #         else:
    #             string += "A"
    #             at += speed
    #             speed *= 2
    #     return string

    # def racecar(self, target: int) -> int:
    #     def distance(i):
    #         return pow(2, i) - 1
    #
    #     if target == 0:
    #         return 0
    #     iterator = 0
    #     string = ""
    #     at = 0
    #     speed = 1
    #     while distance(iterator) != target:
    #         if iterator >= 0 and distance(iterator) < target <= distance(iterator + 1):
    #             diff1 = target - distance(iterator)
    #             diff2 = distance(iterator + 1) - target
    #             if diff1 < diff2:
    #                 string += "R"
    #                 target = diff1
    #                 iterator = 0
    #             else:
    #                 string += "A"
    #                 iterator += 1
    #         if distance(iterator) < target:
    #             string += "A"
    #             iterator += 1
    #             at += speed
    #             speed *= 2
    #         else:
    #             string += "R"
    #             target = at - target
    #             speed = -1 * (speed // abs(speed))
    #             iterator = -1
    #             iterator += 1
    #     print(string)
    #     return len(string)

    """
    Revision 2 :
    This is my second attempt at this question. In the previous attempt I remember leaving the question for later.
    
    Revision 2.1:
    This is by far the most difficult problem I have encountered, specially among the ones I have solved.
    The algo however was easy in the revision time. I figure out how it was a BFS problem.
    The issue however remains of optimisation because for 5478, it TLEs.
    That optimisation comes from a very basic logic, which I have no justification for.
    There are two configurations of (position, speed) which can't possibly lead to the target.
    1. A position greater than target with speed > 0 and heading further away from it.
    2. A position less than target with speed < 0 and heading further away from it.
    These are the two conditions we need to avoid.
    So whenever we reach near target such that we are at the behest of crossing it, we need to fork.
    1. We either proceed and eventually turn back
    2. We need to turn back and retrace and eventually turn back again. 
    """
    # Accepted 60%
    def racecar(self, target: int) -> int:
        queue = [(0, "", 0, 1)]
        visited = set()

        while queue:
            h, moves, position, speed = heapq.heappop(queue)
            if position == target:
                print(moves)
                return len(moves)
            if (position + speed, 2 * speed) not in visited:
                visited.add((position + speed, 2 * speed))
                heapq.heappush(queue, (len(moves) + 1, moves + "A", position + speed, 2 * speed))
            if (position, -1 * speed/abs(speed)) not in visited and ((position + speed > target and speed > 0) or (position + speed < target and speed < 0)):
                visited.add((position, -1 * speed/abs(speed)))
                heapq.heappush(queue, (len(moves) + 1, moves + "R", position, -1 * speed/abs(speed)))


    # def racecar(self, target: int) -> int:
    #     queue = [(0, "", 0, 1)]
    #     visited = set()
    #
    #     while queue:
    #         h, moves, position, speed = heapq.heappop(queue)
    #         if position == target:
    #             print(moves)
    #             return len(moves)
    #         if (speed > 0 and position + speed < target) or (speed < 0 and position + speed > target):
    #             if (position + speed, 2 * speed) not in visited:
    #                 visited.add((position + speed, 2 * speed))
    #                 heapq.heappush(queue, (len(moves) + 1, moves + "A", position + speed, 2 * speed))
    #         else:
    #             if (position, -1 * speed/abs(speed)) not in visited:
    #                 visited.add((position, -1 * speed/abs(speed)))
    #                 heapq.heappush(queue, (len(moves) + 1, moves + "R", position, -1 * speed/abs(speed)))
    #             if (position + speed, -1 * speed/abs(speed)) not in visited:
    #                 visited.add((position + speed, -1 * speed/abs(speed)))
    #                 heapq.heappush(queue, (len(moves) + 1, moves + "AR", position + speed, -1 * speed/abs(speed)))

if __name__ == '__main__':
    print(Solution().racecar(330))
    print(Solution().racecar(5478))
