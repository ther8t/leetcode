import collections
import functools


class Solution:
    def strangePrinter(self, s: str) -> int:
        cache = {}

        def turns(s):
            if not s:
                return 0
            if s in cache:
                return cache[s]
            selected_char = s[-1]
            cost = turns(s[0: -1]) + 1

            for index, char in enumerate(s[0:-1]):
                if char == selected_char:
                    cost = min(cost, turns(s[0: index]) + turns(s[index: -1]))

            cache[s] = cost
            return cost

        return turns(s)



    # # Wrong Answer : 88/200
    # def strangePrinter(self, s: str) -> int:
    #     def turns(lo, hi):
    #         if lo == hi:
    #             return 1
    #         counter = collections.Counter(s[lo: hi])
    #         sorted_counter = sorted(counter, key=lambda x: counter[x], reverse=True)
    #         selected_char = sorted_counter[0]
    #         ptr1, ptr2 = lo, lo
    #         sum_subturns = 0
    #         while ptr1 < hi and ptr2 < hi:
    #             if s[ptr1] == selected_char:
    #                 ptr1 += 1
    #                 continue
    #             ptr2 = ptr1
    #             while ptr2 < hi and s[ptr2] != selected_char:
    #                 ptr2 += 1
    #             sum_subturns += turns(ptr1, ptr2)
    #             ptr1 = ptr2
    #         return sum_subturns + 1
    #
    #     out = ''
    #     last_char = ""
    #     for char in s:
    #         if char == last_char:
    #             continue
    #         else:
    #             out += char
    #             last_char = char
    #     s = out
    #     return turns(0, len(s))



    # def strangePrinter(self, s: str) -> int:
    #     ptr1, ptr2 = 0, len(s) - 1
    #     s = list(s)
    #
    #     turns = 0
    #     while ptr1 < ptr2:
    #         if len(s) == 0:
    #             return 0
    #         if len(s) == 1:
    #             return 1
    #         counter = collections.Counter(s)
    #         sorted_counter = sorted(counter, key=lambda x: counter[x] if x != '#' else -float('inf'), reverse=True)
    #         the_chosen_one = sorted_counter[0]
    #         for i in range(len(s)):
    #             if s[i] == the_chosen_one:
    #                 s[i] = '#'
    #
    #         while ptr1 < len(s) and s[ptr1] == '#':
    #             ptr1 += 1
    #
    #         while ptr2 >= 0 and s[ptr2] == '#':
    #             ptr2 -= 1
    #
    #         turns += 1
    #
    #     return turns


    # # TLE earlier but after DP, wrong answer
    # def strangePrinter(self, s: str) -> int:
    #     dp = {}
    #
    #     def turns(lo, hi):
    #         if (lo, hi) in dp:
    #             return dp[(lo, hi)]
    #         if lo == hi: return 1
    #
    #         dp[(lo, hi)] = min((0 if s[hi] in [s[lo], s[hi - 1]] else 1) + turns(lo, hi - 1), (0 if s[lo] in [s[lo + 1], s[hi]] else 1) + turns(lo + 1, hi))
    #         return dp[(lo, hi)]
    #
    #     return turns(0, len(s) - 1)

    # def strangePrinter(self, s: str) -> int:
    #     s = ''.join(a for a, b in zip(s, '#' + s) if a != b)
    #
    #     dp = [[0] * len(s) for _ in range(len(s))]
    #
    #     for i in range(len(s)):
    #         dp[i][i] = 1
    #
    #     for hi in range(len(s)):
    #         lo = 0
    #         for i in range(lo, hi + 1):
    #
    #
    #
    #     def turns(lo, hi):
    #         if lo == hi:
    #             dp
    #             return 1
    #
    #         dp[(lo, hi)] = min((0 if s[hi] in [s[lo], s[hi - 1]] else 1) + turns(lo, hi - 1), (0 if s[lo] in [s[lo + 1], s[hi]] else 1) + turns(lo + 1, hi))
    #         return dp[(lo, hi)]
    #
    #     return turns(0, len(s) - 1)

    """
    Revision 2:
    I applied for Google today. Finally!!
    I solved this question in one go. I had the logic in my mind. However there is one aspect I am yet not clear about.
    The logic dictates that I select a character to print first as a base layer and then recur for subsequent layers.
    Since layers can only be the same character, we find the character same as the selected character throught the string and find the minimum cost.
    """
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        simplified_s = s[0]
        """
        I recognised it later while solving the question that I was coding a loop to skip over same characters. which essentially does : aaabbccc -> abc.
        The simplified string works wonderful magic.
        """
        for i in range(1, n):
            if s[i] != simplified_s[-1]:
                simplified_s += s[i]

        @functools.lru_cache(None)
        def turns(s):
            n = len(s)
            if not s:
                return 0
            first_char = s[0]
            count = turns(s[1:]) + 1
            for i in range(1, n):
                if s[i] == first_char:
                    """
                    The question that every comment section keeps repeating is:

                    Why do we have dp(i, j) == min(1 + dp(i + 1, j), dp(i, k) + dp(k + 1, j))
                    
                    Instead of doing dp(i, j) == min(1 + dp(i + 1, j), 1 + dp(i + 1, k) + dp(k + 1, j))
                    
                    The second recursion, if it worked, is clearly true, since it matches the explanation and the usual template for dp.
                    Fortunately, your intuition is right! The second formula not only works, but works as fast as and simpler than the popular recursion. The key is to
                    
                    Slightly reframe the question
                    Make the code match the explanation
                    Avoid hidden assumptions about our subproblems
                    Now, what's the hidden assumption being made? It's about what the current printed character is on our interval. The bad recurrence involving dp(i, k) has a hidden assumption that we've already painted the interval [i, k) with the character at s[k], but that we haven't paid the cost for that print yet. This leads us to the new problem definition:
                    
                    dp(i, j) is the number of turns needed to print s on the interval [i, j), given that all of [i, j) currently has s[j] printed over it.
                    From here, the formula is obvious, and can be extended to similar dp problems:
                    https://leetcode.com/problems/strange-printer/discuss/1220646/Rephrase-the-problem-for-a-simpler-recurrence%3A-a-detailed-proof
                    """
                    count = min(count, turns(s[1:i]) + turns(s[i:]))
            return count

        return turns(simplified_s)




if __name__ == '__main__':
    print(Solution().strangePrinter(s = "abc"))
    print(Solution().strangePrinter(s = "tbgtgbt"))
    print(Solution().strangePrinter(s = "aaabbb")) #2
    print(Solution().strangePrinter(s = "aba")) #2
    print(Solution().strangePrinter(s = "abcabc")) #5
    print(Solution().strangePrinter(s = "leetcode")) #6
    print(Solution().strangePrinter(s = "ccdcadbddbaddcbccdcdabcbcddbccdcbad")) #17
    print(Solution().strangePrinter(s = "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"))
