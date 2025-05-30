class Solution:

    # def minNumberOperations(self, target) -> int:
    #     minimum=0
    #     ptr1, ptr2 = 0, 1
    #     count=0
    #     while ptr1<len(target) and ptr2 < len(target):
    #         while ptr2<len(target) and target[ptr2] == target[ptr2 - 1]:
    #             ptr2+=1
    #         if ptr2 < len(target):
    #             coefficient = (target[ptr2] - target[ptr2 - 1])//abs(target[ptr2] - target[ptr2 - 1])
    #             while ptr2<len(target) and coefficient*(target[ptr2] - target[ptr2 - 1]) >=0:
    #                 ptr2+=1
    #         minimum += max(target[ptr1:ptr2])
    #         count+=1
    #         ptr1 = ptr2
    #     return minimum - (count - 1)*min(target)

    # # TLE
    # def minNumberOperations(self, target) -> int:
    #     if len(target) == 0:
    #         return 0
    #     if len(target) == 1:
    #         return target[0]
    #     minimum_elevation = min(target)
    #
    #     for index in range(len(target)):
    #         target[index] -= minimum_elevation
    #
    #     ptr1, ptr2 = 0, 0
    #     while ptr1 < len(target):
    #         while ptr1 < len(target) and target[ptr1] == 0:
    #             ptr1 += 1
    #         ptr2 = ptr1
    #         while ptr2 < len(target) and target[ptr2] != 0:
    #             ptr2 += 1
    #         minimum_elevation += self.minNumberOperations(target[ptr1:ptr2])
    #         ptr1 = ptr2
    #     return minimum_elevation

    # """
    # Memory Limit Exceeded : This is a similar algo as the above recursive code. This is iterative.
    # """
    # def minNumberOperations(self, target) -> int:
    #     if len(target) == 0:
    #         return 0
    #     if len(target) == 1:
    #         return target[0]
    #     minimum_elevation = min(target)
    #
    #     delimiters = [-1]
    #     for i in range(len(target)):
    #         if target[i] == minimum_elevation:
    #             delimiters.append(i)
    #     delimiters.append(len(target))
    #
    #     for index in range(len(target)):
    #         target[index] -= minimum_elevation
    #
    #     for i in range(len(delimiters) - 1):
    #         minimum_elevation += self.minNumberOperations(target[delimiters[i] + 1:delimiters[i + 1]])
    #     return minimum_elevation

    def minNumberOperations(self, target) -> int:
        ans = 0
        target.append(0)
        for i in range(len(target) - 1):
            ans += max(target[i] - target[i + 1], 0)
        return ans


    """
    Attempt: Fired
    Accepted
    """
    def minNumberOperations(self, target) -> int:
        ans = 0
        target = target + [0]

        for i in range(len(target) - 1):
            ans += max(target[i] - target[i - 1], 0)
        return ans

    def minNumberOperations(self, target) -> int:
        ans = 0
        stack = []

        for height in target:
            while stack and height > stack[-1]:






if __name__ == '__main__':
    target = [3,1,5,4,2]
    print(Solution().minNumberOperations(target))
    print(Solution().minNumberOperations([3,1,1,2]))
    print(Solution().minNumberOperations([1,2,3,2,1]))
