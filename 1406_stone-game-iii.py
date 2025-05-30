import functools


class Solution:
    """
    Revision 2:
    This is even cleverer than my solution this time. The score of Alice at the end of the game would be the sum of all the stones - max score that Bob can possibly have.
    At each step. The max score a player can have is the (sum of all the stones till that point - the minimum score I can pick out of the next three.
    Think of this as letting your opponent choose their best move and you then choosing the worst move out of their best moves.
    This is sheer genius move!
    """
    def stoneGameIII(self, stoneValue) -> str:
        dp = [0 for i in range(len(stoneValue) + 3)]

        arrsum = 0  # arrsum aggreagtion from the end to avoid repetitive sumation
        for i in range(len(stoneValue) - 1, -1, -1):
            arrsum += stoneValue[i]
            dp[i] = arrsum - min(dp[i + 1], dp[i + 2], dp[
                i + 3])  # we want to maximize the value for current player so we need to minimize the gain for next player

        score = dp[0]  # dp[0] is the maximum gain for player who plays first
        """
        I am surprised by the use of 2 * score - arrsum. I have done the same problem below with arrsum - score and it was ACCEPTED.
        """
        s = score * 2 - arrsum
        if s > 0: return 'Alice'
        if s == 0: return 'Tie'
        if s < 0: return 'Bob'

    """
    Revision 2:
    
    Accepted 63.5%
    I guess this is another take on the above solution. Although I haven't really read the above one.
    My idea here is to find the best move at each step, irrespective of either Alice or Bob. Assume they ask a supercomputer for aid.
    The best move at a point is to choose between the sum of 1, 2 or 3 stones plus the best move which the current player would take next. Which means the move next to the next move.
    Thus sum(1,2 or 3) + best_move(1,2 or 3 + stones_chosen for the next best move)
    
    The idea was simple enough but I made one grave error.
    The dp is basically an aggregation of all the moves. What I did instead was to sum up all the scores. I had forgotten this part. The max sum of alice would be dp[0] not the sum of his planned moves.
    And the max sum bob can have is dp[0 + stones_chosen[0]], and not the sum of all the moves further down.
    With that sorted I had the solution at hand.
    """
    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)
        dp = [-float('inf')] * n
        stones_chosen = [0] * n
        stones_chosen[-1] = 1
        dp[-1] = stoneValue[-1]

        for i in range(n - 1, -1, -1):
            for j in range(1, 4):
                if i + j > n:
                    break
                current_score = sum(stoneValue[i: i + j]) + (dp[i + j + stones_chosen[i + j]] if i + j < n and i + j + stones_chosen[i + j] < n else 0)
                if current_score > dp[i]:
                    dp[i] = current_score
                    stones_chosen[i] = j

        scores = [dp[0], dp[0 + stones_chosen[0]] if stones_chosen[0] < n else 0]

        if scores[0] == scores[1]: return "Tie"
        return "Alice" if scores[0] > scores[1] else "Bob"


    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)

        aggregated_sum = 0
        for i in range(n - 1, -1, -1):
            aggregated_sum += stoneValue[i]
            dp[i] = aggregated_sum - min(dp[i + 1], dp[i + 2], dp[i + 3])

        alice, bob = dp[0], aggregated_sum - dp[0]
        if alice == bob: return "Tie"
        return "Alice" if alice > bob else "Bob"





    # # TLE 181/185
    # def stoneGameIII(self, stoneValue) -> str:
    #     def best_move(position, turn):
    #         if position >= len(stoneValue):
    #             return 0, 0, 0
    #         if turn == "Alice" and dp[0][position][0] > 0:
    #             return dp[0][position]
    #         if turn == "Bob" and dp[1][position][0] > 0:
    #             return dp[1][position]
    #         stones_chosen = 0
    #         max_a_score = -float('inf')
    #         max_b_score = -float('inf')
    #         for i in range(1, 4):
    #             # if position == 2 and i == 1:
    #             #     print("a")
    #             current_score = sum(stoneValue[position: position + i])
    #             next_move_stones, alice_score, bob_score = best_move(position + i,
    #                                                                  "Bob" if turn == "Alice" else "Alice")
    #             if turn == "Alice" and current_score + alice_score > max_a_score:
    #                 stones_chosen = i
    #                 max_a_score = current_score + alice_score
    #                 max_b_score = bob_score
    #
    #             if turn == "Bob" and current_score + bob_score > max_b_score:
    #                 stones_chosen = i
    #                 max_b_score = current_score + bob_score
    #                 max_a_score = alice_score
    #         if turn == "Alice":
    #             dp[0][position] = stones_chosen, max_a_score, max_b_score
    #             return dp[0][position]
    #         else:
    #             dp[1][position] = stones_chosen, max_a_score, max_b_score
    #             return dp[1][position]
    #
    #     ptr1 = 0
    #     dp = [[[0, 0, 0] for _ in range(len(stoneValue))] for _ in range(2)]
    #     turn = "Alice"
    #     alice_score, bob_score = 0, 0
    #     while ptr1 < len(stoneValue):
    #         stones_chosen, a_score, b_score = best_move(ptr1, turn)
    #         alice_score = sum(stoneValue[ptr1:ptr1 + stones_chosen]) + alice_score if turn == "Alice" else alice_score
    #         bob_score = sum(stoneValue[ptr1:ptr1 + stones_chosen]) + bob_score if turn == "Bob" else bob_score
    #         turn = "Alice" if turn == "Bob" else "Bob"
    #         ptr1 += stones_chosen
    #
    #     if alice_score == bob_score:
    #         return "Tie"
    #     else:
    #         return "Alice" if alice_score > bob_score else "Bob"










    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)

        @functools.lru_cache(None)
        def search(index):
            if index == n:
                return (0, 0)
            max_score = float("-inf")
            second_score = 0
            for i in range(index, min(index + 3, n)):
                my_score, others_score = search(i + 1)
                if my_score + sum(stoneValue[index:i + 1]) > max_score:
                    max_score = max(max_score, my_score + sum(stoneValue[index:i + 1]))
                    second_score = others_score

            return second_score, max_score

        b_score, a_score = search(0)
        if a_score > b_score:
            return "Alice"
        if a_score == b_score:
            return "Tie"
        return "Bob"


if __name__ == '__main__':
    print(Solution().stoneGameIII(
        [-7, 17, -2, -13, -6, -7, -13, 11, -3, 15, 0, -11, -5, 1, 2, 13, -14, -16, 1, -8, 6, -2, -14])) #Alice
    print(Solution().stoneGameIII(
        [-10, -9, -6, -11, 12, -15, 5, 4, -9, 9, 6, -5, 12, 16, -3, 9, 0, 13, 1, -10, 6, -14, 13])) #Alice
    print(Solution().stoneGameIII(
        [1, -14, -14, -11, 7, 5, -10, 9, 3, -9, -1, 9, -4, 14, -8, -15, -15, 10, 9, -13, -8, -17, -5])) #Alice
    print(Solution().stoneGameIII([1, 2, 3, -9])) #Alice
    print(Solution().stoneGameIII([1,2,3,7])) #Bob
    print(Solution().stoneGameIII([1,2,3,6]))#Tie
    print(Solution().stoneGameIII([9,-4,0,12,-5,-13,15,6,-16,8,2,16,12,-6,13,0,-16,-11,9,-14,7,-1,14])) #Bob
    print(Solution().stoneGameIII([-2])) #Bob
