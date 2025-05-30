class Solution:
    """
    Revision 2:
    I got the logic pretty quickly but the one thing which I made a mistake on is that I considered that they are arranged in the order of index.
    They would actually be arranged in the order of position. Duh!!
    So I had to sort this and then it became the problem of a monotonic array.
    """
    def carFleet(self, target: int, position, speed) -> int:
        combined = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        combined.sort()
        stack = []
        for i in range(len(combined)):
            while stack and combined[stack[-1]][1] <= combined[i][1]:
                stack.pop()
            stack.append(i)

        return len(stack)

    # def carFleet(self, target: int, position, speed) -> int:
    #     combined = list(zip(position, speed))
    #     combined.sort()
    #     fleet_count = 0
    #
    #     max_time = -float('inf')
    #     ptr = len(combined) - 1
    #     while ptr>=0:
    #         p, s = combined[ptr]
    #         time = (target - p)/s
    #         if time > max_time:
    #             fleet_count += 1
    #             max_time = time
    #         ptr-=1
    #     return fleet_count

    # # TLE
    # def carFleet(self, target: int, position, speed) -> int:
    #     combined = [[position[i], speed[i]] for i in range(len(position))]
    #     combined.sort()
    #     fleet_count = 0
    #
    #     while combined:
    #         min_time_taking_car = min(combined, key=lambda x: ((target - x[0]) / x[1]))
    #         destination_time = (target - min_time_taking_car[0])/min_time_taking_car[1]
    #
    #         ptr = len(combined) - 1
    #         combined[-1][0] = combined[-1][0] + combined[-1][1] * destination_time
    #         while ptr >= 0:
    #             distance = combined[ptr][0]
    #             while ptr - 1 >= 0:
    #                 combined[ptr - 1][0] = combined[ptr - 1][0] + combined[ptr - 1][1] * destination_time
    #                 if combined[ptr - 1][0] >= distance:
    #                     combined.remove(combined[ptr - 1])
    #                     ptr -= 1
    #                 else:
    #                     break
    #             if distance >= target:
    #                 fleet_count += 1
    #                 combined.remove(combined[ptr])
    #             ptr -= 1
    #
    #     return fleet_count


if __name__ == '__main__':
    print(Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
    print(Solution().carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
    print(Solution().carFleet(10, [0,4,2], [2,1,3]))
