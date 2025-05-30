import heapq


class Solution:
    """
    Revision 2 : Accepted : 25%. DP. This is an O(n2) solution. This is the first solution which came to me. There is however a better greedy solution available.
    """
    def jump(self, nums):
        dp = [float('inf') for _ in range(len(nums))]
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = min(dp[i + 1:i + nums[i] + 1], default=float('inf')) + 1
        return dp[0]

    """
    Revision 2 : Imagine this for greedy solution. We begin at 0 and try to see till the farthest point it would allow. 
    What do we see for? We see for two things, 
    1. what is the farthest point that can help me reach. 
    2. The number of steps it would take to reach the fatherst point.
    There are two certainties in this. The number of steps it would take from the current position to the farthest point we can reach would be (jumps + 1), 
    where jumps would be the minimum number of steps it would take to reach the current position and (jumps + 1) would also be the minimum till the farthest 
    point from current location.
    For example. [2, 3, 1, 1, 4] Starting at 0. Till index 2(including), the minimum number of steps would be 1 only. the next farthest point would then become (index 1 + 3) index 4, which would have minimum of 2 jumps.
    """
    # Much simple Greedy
    def jump(self, nums):
        farthest = 0
        jump = 0
        currentPosition = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # Not including this if statement makes the code run for lesser iterations but makes it run faster.
            if farthest >= len(nums) - 1: return jump + 1

            if currentPosition == i:
                jump += 1
                currentPosition = farthest
        return jump


    # # Too Complex : Backtracking and DP
    # def jump(self, nums):
    #     dp = [-1 for _ in range(len(nums))]
    #
    #     def backtrack(presentIndex):
    #         if presentIndex == len(nums) - 1:
    #             return 0
    #         if presentIndex >= len(nums) or nums[presentIndex] == 0:
    #             return float('inf')
    #         maxJumps = nums[presentIndex]
    #         minJumps = float('inf')
    #         for jumps in range(1, maxJumps + 1):
    #             if presentIndex + jumps < len(nums):
    #                 if dp[presentIndex + jumps] == -1:
    #                     jumpsRequired = backtrack(presentIndex + jumps)
    #                 else:
    #                     jumpsRequired = dp[presentIndex + jumps]
    #                 if jumpsRequired < minJumps:
    #                     minJumps = jumpsRequired
    #         dp[presentIndex] = minJumps + 1
    #         return minJumps + 1
    #
    #     return backtrack(0)


    """
    Attempt: Fired
    Accepted: 73%
    The idea is to find the farthest place we can reach from the current position because beyond that we would need to make a jump anyway.
    The next jump that we make must be in such a way that it is the farthest possible.
    So, between current position and the farthest that this would allow, we try and find out the farthest we can go beyond that.
    For example:
    [2, 3, 1, 1, 4]
    At i = 0, the farthest we can go is i = 2, so between 0 and 2, how much farther can we jump beyond 2?
    That would be i = 4.
    So after 2, we make a jump to the farthest.
    """
    def jump(self, nums):
        farthest = 0
        jump = 0
        prev_farthest = 0
        # The reason we do len(nums) - 1 and not len(nums), is because if the prev_farthest == n - 1, it would create an additional jump which is unecessary.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if prev_farthest == i:
                jump += 1
                prev_farthest = farthest

        return jump

    """
    Attempt: Fired
    Accepted:20%
    """
    def jump(self, nums):
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums)), 1):
                jumps[j] = min(jumps[j], jumps[i] + 1)
        return jumps[-1]

    def jump(self, nums):
        n = len(nums)
        h = [(0, 0)]

        while h:
            (jumps, i) = heapq.heappop(h)
            i = -i
            if i >= n - 1:
                return jumps

            for j in range(i + 1, min(i + nums[i] + 1, len(nums)), 1):
                heapq.heappush(h, (jumps + 1, -j))

        return float('inf')



if __name__ == '__main__':
    print(Solution().jump([2, 4, 0, 1, 4]))
    print(Solution().jump([3, 2, 1, 0, 4]))
    print(Solution().jump([0]))
