import functools
import time


class Solution:
    # def minWindow(self, s1: str, s2: str) -> str:
    #     def dfs(i, j):
    #         if j == len(s2):
    #             return i
    #
    #         if (i, j) not in dict1:
    #             idx = s1.find(s2[j], i + 1)
    #             return float("inf") if idx == -1 else dfs(idx, j + 1)
    #
    #         # return dict1[(i, j)]
    #
    #     min_len, str1, dict1 = float("inf"), "", {}
    #
    #     for i, s in enumerate(s1):
    #         if s == s2[0]:
    #             j = dfs(i, 1)
    #
    #             if j - i < min_len:
    #                 min_len, str1 = j - i, s1[i:j + 1]
    #
    #     return str1

    # def minWindow(self, s1: str, s2: str) -> str:
    #     dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    #
    #     for i in range(0, len(s2)):
    #         for j in range(0, len(s1)):
    #             if s1[j] == s2[i]:
    #                 dp[i+1][j+1] = dp[i][j] + 1
    #             else:
    #                 dp[i + 1][j + 1] = max(dp[i+1][j], dp[i][j+1])
    #     print(dp)

    # TLE
    # def minWindow(self, s1: str, s2: str) -> str:
    #     if len(s1) == 0 or len(s2) == 0:
    #         return ""
    #
    #     middleIndex = len(s2) // 2
    #     middleCharOccurrence = []
    #     # search for all the occurrences of the character. The first occurrence of the character if it's a contiguous pool of same character.
    #     for i in range(len(s1)):
    #         if s1[i] == s2[middleIndex] and (i == 0 or s1[i - 1] != s2[middleIndex]):
    #             middleCharOccurrence.append(i)
    #
    #     lengthCounter = []
    #     # build around all the middleCharOccurrence
    #     for i in range(len(middleCharOccurrence)):
    #         s1LeftIteratorIndex = middleCharOccurrence[i] - 1
    #         s1RightIteratorIndex = middleCharOccurrence[i] + 1
    #         s2LeftIteratorIndex = middleIndex - 1
    #         s2RightIteratorIndex = middleIndex + 1
    #
    #         while s1LeftIteratorIndex >= 0 and s2LeftIteratorIndex >= 0:
    #             if s1[s1LeftIteratorIndex] == s2[s2LeftIteratorIndex]:
    #                 s1LeftIteratorIndex -= 1
    #                 s2LeftIteratorIndex -= 1
    #             else:
    #                 s1LeftIteratorIndex -= 1
    #         if s2LeftIteratorIndex != -1:
    #             lengthCounter.append((-1, -1))
    #             continue
    #         while s1RightIteratorIndex < len(s1) and s2RightIteratorIndex < len(s2):
    #             if s1[s1RightIteratorIndex] == s2[s2RightIteratorIndex]:
    #                 s1RightIteratorIndex += 1
    #                 s2RightIteratorIndex += 1
    #             else:
    #                 s1RightIteratorIndex += 1
    #         if s2RightIteratorIndex != len(s2):
    #             lengthCounter.append((-1, -1))
    #             continue
    #
    #         # found the supersequence match at [s1LeftIterationIndex + 1, s1RightIterationIndex - 1]
    #         lengthCounter.append((s1LeftIteratorIndex + 1, s1RightIteratorIndex - 1))
    #
    #     minLength = float('inf')
    #     minSubsequenceMatch = ""
    #     for i in range(len(lengthCounter)):
    #         if lengthCounter[i][0] == -1 and lengthCounter[i][1] == -1:
    #             continue
    #         if (lengthCounter[i][1] - lengthCounter[i][0] + 1) < minLength:
    #             minSubsequenceMatch = s1[lengthCounter[i][0]:lengthCounter[i][1] + 1]
    #             minLength = (lengthCounter[i][1] - lengthCounter[i][0] + 1)
    #     return minSubsequenceMatch

    """
    Revision 2 :
    This is amazing question. I had to check if online. The reason being the 'find' function for a string. It's written in C perhaps and because of that it's fast enough to execute a brute force code but not good enough to test your algo skills.
    The real algo is below which I tried for the first time here.
    This algo below is important but the don't worry about the find function.
    """
    # Accepted by 64%
    def minWindow(self, s1: str, s2: str) -> str:
        last_occurrence = [-1 for _ in range(26)]
        next_map = [() for _ in range(len(s1))]

        for index in range(len(s1) - 1, -1, -1):
            next_map[index] = tuple(last_occurrence)
            last_occurrence[ord(s1[index]) - ord('a')] = index

        queue = [i for i in range(len(s1)) if s1[i] == s2[0]]
        score = [[queue[i], queue[i]] for i in range(len(queue))]

        for char in s2[1:]:
            for i, index in enumerate(queue):
                if index == -1:
                    continue
                next_index = next_map[index][ord(char) - ord('a')]
                queue[i] = next_index
                score[i][1] = next_index

        if not len(score):
            return ""
        x = min(score, key=lambda x: x[1] - x[0] if x[1] > x[0] else float('inf'))

        return "" if x[1] < x[0] else s1[x[0]:x[1] + 1]


    # def minWindow(self, s1: str, s2: str) -> str:
    #     if len(s1) == 0 or len(s2) == 0:
    #         return ""
    #     recordKeeper = []
    #
    #     minLengthSubsequence = float('inf')
    #     for i in range(len(s1)):
    #         if s1[i] == s2[0]:
    #             t = time.time()
    #             matchLength = self.matchMinSubsequence(s1[i + 1:], s2[1:])
    #             print(time.time() - t)
    #             if matchLength == float('inf'):
    #                 continue
    #             recordKeeper.append((i, matchLength + 1))
    #             minLengthSubsequence = min(minLengthSubsequence, matchLength + 1)
    #
    #     for i in recordKeeper:
    #         if i[1] == minLengthSubsequence:
    #             return s1[i[0]:i[0] + i[1]]
    #     return ""
    #
    # def matchMinSubsequence(self, s1, s2):
    #     if len(s2) == 0:
    #         return 0
    #
    #     target = s2[0]
    #
    #     searchResult = s1.find(target)
    #     if searchResult is not -1:
    #         return searchResult + 1 + self.matchMinSubsequence(s1[searchResult+1:], s2[1:])
    #
    #     return float('inf')

    # def matchMinSubsequence(self, s1, s2):
    #     matchLength = 0
    #     index = 0
    #     while index < len(s1) and matchLength < len(s2):
    #         if s1[index] == s2[matchLength]:
    #             matchLength += 1
    #         index += 1
    #     return index if matchLength == len(s2) else -1


    def minWindow(self, s1: str, s2: str) -> str:
        """
        Revision 2.1:
        This is a brute force solution to the problem. There is a better algorithm available. It's written above. But this is what came to me.
        """
        def match(s1_index, s2_index):
            if s1_index > len(s1):
                return s1_index, float('inf')
            if s2_index == len(s2):
                return s1_index, s1_index
            match_index = s1[s1_index:].find(s2[s2_index])
            if match_index != -1:
                start, end = match(s1_index + match_index + 1, s2_index + 1)
                return s1_index, end
            return s1_index, float('inf')

        min_length = float('inf')
        out = ""
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                start, end = match(i + s1[i:].index(s2[0]) + 1, 1)
                if end != float('inf') and end - start < min_length:
                    min_length = end - start
                    out = s1[start - 1: end]
        return out
































    """
    Attempt: Fired
    Accepted: 55%
    The only time saving from this and the obvious solution of finding the first index and matching the rest of the subsequence is the forward lookup.
    Find makes it faster to lookup forward.
    """
    def minWindow(self, s1: str, s2: str) -> str:

        def match(s1_index, s2_index):
            if s2_index == len(s2):
                return s1_index
            if s1_index == len(s1):
                return float('inf')
            search_result = s1[s1_index:].find(s2[s2_index])
            if search_result != -1:
                return match(s1_index + search_result + 1, s2_index + 1)

            return float('inf')

        min_len = float('inf')
        ans = ""
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                end_index = match(i + 1, 1)
                if end_index != float('inf') and end_index - i < min_len:
                    min_len = end_index - i
                    ans = s1[i:end_index]

        return ans








if __name__ == '__main__':
    print(Solution().minWindow(
        "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa",
        "fffessa"))
    print(Solution().minWindow(s1 = "abcdebdde", s2 = "bde"))
    # print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "k"))
    # print(Solution().minWindow("cnhczmccqouqadqtmjjzl", "mm"))
    # print(Solution().minWindow("hpsrhgogezyfrwfrejytjkzvgpjnqil", "tgr"))
    # print(Solution().minWindow(s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"))
    # print(Solution().minWindow(
    #     "faalafealefelfafaleflflaeelleaelefafelflfeefaafaalleeeaflfaaeeleeallaaeeffffllalfafalfaelffffeeallaafeelfeelefelafaefafleeflfefeellllfffellleealflaaaellaeaefeaeeeealeflfafefafeeefellaalelllaefelefaeaallleealllealaleealfeeaaeaefeaefllaeefeaflaeeflaelllffeleleeeefeaaeflefllleefelfaeafeaaaaeeffaalflefleelaeeffleelffaeaeeaaleeaelaeaeeflafafelfaelflfllaealffealeeefafleaaflfelelalaealaaaalfelaaelflallefeaellelleeellaeaeaflaflllelaaeelfeaeeeelalffelefllaeeaaflaaeafeflflaeelaalaaaefefaaalfflaaeflfalefaefeffllaffaflffefeaellfalallfeelefeellellllaaaffalflaeleleeefellfaelfleealaaeafeafeaalflaafaaaeffellfflfafealafealeallfelaeafffeefaffafllleeeflaalafallaeaaaffefallallellaflflaalflaaelellelflaaaeeelffaalalealaeaeeleaafafflfaflefeaffalllfaelaaaaelffeealffffllaaafffeffaaaaaaaaaefllefeellaealalfallaffeffaafleeleelfeaallaleeealfeeflfflefeaalfeaaaaaallllaelfleefffealflaafffllllaaellfafefeelfalalaafllfaelffflleeafalflaealfefaelleeffelaaaaflelffaleaaeafallaaaaellfaaalfaalflefeaaflfalfaelllelealaefefeellaaeelefaelefefefllalaeaaafaaealfaaeeeleaalflelfalffffeaaefeefleeaeeelelflffaeleffaaffeealallaaaeelealeeeleaaaflflfllafelafeelfaaaefaaeffeefalfafffaeelleeleafeeeeaeeefalffaalfelaalealelafffalfelfallaaaeaafaflalealfeflafffeeelfalaaelaefeelefaleefaelfaaalfaleffellfefaaelafeeaaafaeffeleeaflafafeeaelfffeeaaaeeflafafelelaeeleeleffallleeleleelaeflffaelaaeelaafeleefaelleaeffflfflffeaeffllefleellaaallalaellelaefaellallllefffaefefefaefaaalefellaefeeealealeefafaeaaalaefeafllaffflalflfaaffffaleellefaffaefeelfllllaaeefallaafefeaalfeaelfaeleaflalaafafflflffffaflalefllfefleaefalelflffalfllaallellellllffaeefeffaallfeafafeelaeaeefffaellffffafaflefafllaeflflaaalalalealleflaeeeeleaaleffllaalaffefeflalalafleeleallaeeaaeaaaflleeaalaelleeflaelllaaaeflffefeealeeeefaaeeelalaealffaaeealfefeafeaafeaafleeaffleellaaellfalfeaeafaleelafallaeeflaafflfffaleelffllaffelleellefeeefllaealfllflfaeafaellaeaalalellaefaafeelflelllaaffalfeaaealflaaaaefllealllellllfefflalflffallfaafafafllaealllaellffalefafaeflelellffeefafefleelaeeeleeefeeleffflefalalaaaflfellflafeaelalaeflleallefalaffffafealllllleaeffaalleelaffeaffeafalafelfafaeefllfffellafallfefffalalflaeaallaffefllalflealeeelaallffflaefefafeaellleeflafaleaaefaelaaeafleeaafafflfaalelelfeaeffaellefelfeaeleeleeleeefalffaeeaaeeafelafleeeleaflefalfallffelafeleaalalllelaeeaaefaafflaffelefafflellaefeffleaelleffeafaefaffaeflfeelffaaffeffafaeealeeeeeflefeffealaaleleaallaelfafflfefaleaelefafffaeaalfelaeeffaelfeffaefflaaflaaaafelffefeeffeffeaflaeefllalelefffeflafeealaeelealaaaaeeallllaefelalaeffeeaaleeeefaaffaeeaffleeeelflaaellafaelfalellalfeaeeeelaefflaaallfefeeeellafefllflllfafeelfffefeaaffflafeleeefflalalfeeefaelaaleaallfffeflfealelaefaaealeafaffaffefffaafalaleefaafalelelleaeelflaefffaffeefelflaflefllfaafeeleleleffalalfelfafaeafeaaaaeelfllllafffeeelfelafealaflflflafafaaeeefaafeffefaleeelfeaefffaflllaealefaalaefaalaafaaelflefllafefaaaflfaeafleffaflfleaafaelaafleallfffalafaaleeeaeflaaefaelafefalfafalaefeffllalllleeaallaaffeeafaaaffllfaleaflaelllllffaeeaeaaaalfffaffelfaaaefeefaflfaflaaeealaleaaafeeelaeffeelaefaffaffaafaaffleflfalalalefalellaaaaeaffflfafaalelffeeaeaafalalafllaafeffefalfeffelfaflaafellffafeeaflalaaaaafeflllefefllaleeeeefeleaafelfefafffeffllllafaaafeefleaeaefflelfaffaefleefeelfalaflelaalfleeaeaafalaaeellfaelflfaeaeelffallllleeaeaeaffaaleeellaaelefleaalllaaflfeeafalfefllaafllfalaeeeefeffeeafleaflaalafalaleaaeefflalfleffalafeelfaaleeaeeefaaalefallleefffaaaaeealafeaeeleaeeelafflafelaafffaafeaffeefefeaaaeelffalleeefefefalfllafelalleefllaaleffflaelflfeaflfeeefafaelalllaaeelalleaafleflfeeaefelflelfeflllalleefafeelelealaaaaealfflfaeafleaeffllaleeaeeaaleaeaflafffelllaaleefeaflffllaaaflaleeflafaffealeelaeaeeaelfafeaffelelflaaallllelfeleeaaleaaffaeafeefellfaeleelfflalaaaffaeefallfeaaleaeflffflellelffeaefellaeflffellelflflalfefeaafllelaealaafaafafeffeleaaflfafefelefeaeefeefefafeaaaeaeeaealelaeflfaleeefllflflellealalaefeafaffelfealaeleeealflfafleafefffffaleaeaaelaeeaeffflllleeffelfaleefaalfealfflefalallaleelefeeflaafalffaflfelffafllelflafllfllafpopxorpproppprooxoxxoxrxoxrppppxroroorxrrxorporxoprrxxprporopxoxrpxpxoxroxrxrproooppooppprppxrorrxxooxrooxoppoprorprxpxrxoxpxorppppopxrxroooprxooxxxpxoropoxoxxxropprrpxoprrrooopppxppxrxpprpxoppprxorxorxoroxxrprrpppxrrxrrroxorpxrpooppoxrrpopoppxrrxoxorppxoxxrpxxxrprxrxooprxxprxrrproxrrrrpprpooorrxrxpprpropppooprrpxxroooproooxxoxxoxopoorpoxxrpoxprpporpxooxxxrxopoxpxpxorxorprxoxrxxorxprpooxrppxoxorppxxorpxxrxrrrpopxxoropprrproroxxrppporrrxoxrxroroorrppprpxropppxprororoppxprpxopprpprpppoxooxpopprrrpxpoxppppxxoorxporoxoxxppooxooroxxoxporxxxrprpppoxrpoprxxroprxxppporxrxrrrpopxxppxxxoxxopoxrrporpxpoopxxxxxopxpprprpxpproxxoroxppppxppoxpoxoprxpxrrpprxpxxrxxpoxpxxxxrorxpxxrorprrrorroxxoxxprorpprrpoorroxpxoxpxoopooxpppxrrorprropxorproxrxpprrrpxxoroporxxropxxxxooopxrrxproppprxxoooopxrrxppoxoxrrxooopoxpooxxooxppoxpooorpxxxpooxooxoopxxxporxoxxrprxppopxrrororxrxrxoxxorrxrorrxopxxprxxroxxropopxxorrxrrxpopxopporrxroopprpxoxororrpxororxxxxpopoxrrxrxxopoppooxpoxorxrrrorporxooppxoxoxoxxopxxoxrpxppppxrrprxoxrxxprxxxxpproopoooorrprpopoorprpoxporxpooxorproooppoxropoxorprrprxroropxrxrorpoorxxxprxooxoorrpxporxoooxxrxxoxpxrrxpproppprorroorxxrprxrorxrpoorprroooroxxrrorooxxoopxoopororopooxpoxxxpproporpopoxrppxxxpoxrrpoxxrrxororopprorooroxopoorxxpxrpxrxrxrxprxrrxxoxrrpoxxrrpxxoroxxrppxpxpxrpppoopprrxrrxororopxpoxxorrroprorooooorxxoxrxxoporropopxrrorpopoooxrrrpporpprpxoxxrppxrrorppxprpooxoxxpxrrproporrxxppxprxrrrroorrrxproxopxrorrropxrxoprporropoppprrrxpxopoorpooxprooooxroxooprrropxpxxxrrppxpororoorprroxrrrxppxppprropprroxrorroprxxpxxoxroopxrproprrpoxporprrrprpropxprrrrrpppoxpxoroxpxorprprxrprorrxpxrrorpxoxoxxorrroprroxrxpxrrppxporoxpooxxxxpxopooroopprxpoorprrpoopppxorrprxpprorxxorooppxrroxoxoopoxxppoporrxrrrxpxrprppopxrooppppoxoppxorxoxrxxoproxxpprrorpoppxrxpxrroxxorrrppproorroxrxroxxrroprxrpoprooppprxrpproprpxrrprrrpxpxpxrxrxrpxpoprxoroxoroorrprxxrpxpoppxoporxxrxxxopxpoxxppoxooroxprxrrppxpropprpxpppororrxorooxrororrrpprppopxoorprpxrorrxxppoopxopoooropoxrrpprpxxppxprproorpporpooxoxrorxropppxoxoorpxrrrrpxropoxxxpoxoooxppxrxxroooppxrrpppooproxprororrxrorpprpxrprxropppoorxrprorprrorxxooxoprorpporppoopxxrxxpprrppxpprroporprroroorpprooooxoxpprrrpoxpppprxoorooooprpoororoxprxrpxxxrropprooprrxrorrorrororxxprproxrxxxoxpppoppxpoprporxxpoprrxopprxrxxopxooopporpxrooxxrpoppxrppxoxrroprxppxrxrxrppxopooprooooorpoxopppooprxoxrpxorxxproorporroxoxxxrprxppooorprxxxrpooxopporxrpororprpppxprxorxxororpoorpporxrpopxropxxxxoorppxroooxpoorrppporxpxxrrrpoxpxoxprpxrorroxxxxxxoxpoxpxprrrxooppoprrxrropooprxxxrprxrxoxoroxrpppopxxrxxxxoorrppporxooopopprxrporpprpprrppppoxoxrororpoopxxrorpppoxxrrxooorxrroxxoxoxooxorprooroxrppproxxpxrorpxxprroxxoxprooxpoprrproprrxrpxxoppoxprrroxxpooxrprproxoxrppoxpprxrxxrrorpxopxroroooxroorxxoooxxxprrorxorooroxoprpprrxxroxopoorpxpopopooxpopoopoppoxxoooxxrporprxxxrpxxoxppporxpxorppoprxrppoxpoxopopxpxorxxxooorxprproppooppoooxxppxrpprxpprxpporoooxrrxopoorprppxopxpxxpppproxoppxorrrropoxpooroxpxroorrpoxrxrxpxpoppoxrppxrrpxoporopppxpxoxxppprrorxrrxopxrorooorrrxrrppropprpxpxropoxporrroppxorrxprpxpppoorxoprrproxrooropxoprprprpxppppporrxpoxxrrppxxxoppxxpxxrrproxpoporororrrroxoprpxooxprorropxxrroxrxooxrxxxorxrprprxrxxpxororxxpoxoxopoproppxpxrprxoooxooxrprorxoopprxoooxrrxopprxrxxoppxxoxopoprxxrxoxxxorpooorrxropxoxprpxpopxxpxoxoprxxporopropxorrorpporropopxpxxrrooooprorororrroooprooxorxppoxppxoopoxxoppooxopxrxpxxpoooopppooxooppxrppxxxxpoopoxxoprpoxpprproxpxopprpxxrxxxorrrxxpooorrrprrprxorrxoppopprxxoxxprxrxroooxrorpropxxpxrxorxrpxxropxxoppprrxpoxxxrxxxporpprrrporprpxpxroprrpopxxorpxxpprxooxxorxopxpxppopxxopxoroorxrpoxxrxpooorppopoorxxrppppoorxoxrprxrxopprpxxpxpoxxroorxoppppooxoppoxrrpoxoxxxopooproroprppxproxoxpoxpxpopxoorrpoxrooppxrpxooxxxxrrprooopoxrpxxxxprrpppoppprrporopoxrrprprrpporopproroprooooproxrrxpprpxoxopxxrxprppxxoxxooxpppxorrrpoooopopxxrxoooxoxxrrrprooooopoororrprooxorrxooxopoprrxxrooxrrpproxpxooporxprxxpxpprxproxrxropxpxppxprxrorxroxrpxpopppoxxroropxoxopporpxoxorrppppxxrrorprrorrprorpxpxpppoooorroxrxrporrrxpxpoxxppxroprxpprorrxoroxrrrroppxxopxoropoxxpoxopxssllmmslsmssmallssmsalalmmmslmlalmsssllmasmlmssammaaamlalaalmsammlmasamsmammsssamalalmasssmlasaalsalsllasaammmmsslsllllaamlllllamlslmlllamlsmlallllallalaalsmmlaaasamssmamlamslammsmssalaasmaaaamsllsmllmlasmmmlslmlmsalsllsmlmsaallsaaaaslslsmasalmssaasaamslllmlasmallssslalsaaaasllslamlslmmlassmlaammmmslssmlalamaaalmalssmlsllmsamaaslaslmmlmlllmamlsslmmlmaalalsssmmsssammaalmmaammmllllasasamsmlalallsamllsalsllmssmalmsmlamsalslmmslassalmlaasamamsamsalsllammmmsalsmlsalmlllslsasmalmslsslslslslssmmaasassmssmmlsasmsmllaamlmamsassmaslmsmalaaalsmaamssssamsmmsmasslmsmmmlsaaamlmsasssmllssslalamlasmlasssmsmmsalsmssmsmllslalmmammsslaalllsmllmmmlsllmammmlamlaslsmmasamsamlsamssmalmsmslmlassmmmmmlmmslsalsllaaamalaslamsmamsssmasmammmllamlmaallssmmsassallmlsalamlalsmmlsaasllmlalmmmslammamsalsallslamlmsmallmmaaasmasalmlslmlsmmmasaamalsalaalalmsaammasmmaalssmmaasssllmamlmsssallssslmlmamlllsalammsmamaammmlasmmamllmllmammammlamlslammmllllssllassmmsmaslasssaassslmllmlalmllalmaaaamalmlsaalsssaamamllmamsammssssaaalsmaaamlmlsaassalaassslsalalsmasamaslalslalmasllssllaallsssalasamssmsalallaammlalmmmaammalaslmmlsamlllmsmasamlmaammmamalamlsllamlmsmmlllasmasmalaaasslmsllmlmmllsasmllssmllsmlssmamslssmmamsmssslsmlsmllllmaalsmmalalslsasmmamsmssalaasmallmsllssmlaslalallmassssamsmmalmasslssaaalslmsllsmmmssalmlsslaasmllmmlaalmsmlaassaslsmsmlmsslmslaasalmasslaslamasmmsmmlllsalsmmmaslalmmlaamalalslsalslmaslsslasalllmmlamamalmasssllasmlassalllmsmmlsamsammslallmssssamamamaamlmssmassmslammmlmalssllmmslmassllsmmaaslsaalmlaamaalsmlmaammmlsmlassmmlmmmasmasallmlalassasamslsaalsmsammalmlamsmllsmmmmasasllssslassallmmsmasaaalasllmlmsllsammmlasmlsammamaaaslsmlsalssllalsaamalmlsmaasaasmlaamallamlammsslalaslalsallamlmamsalmmaslsmaalsmllaasaassassllaasmsslamlllmmssslasllmsamallassamsmmsamlmamaslsaalsmmlsaaamllallaslsamlsalaasalassmlalsllmlmaslammallasaammsamssmlaslsmslalmlmlsaallaamalalslmmssallmlmsslasssmllslalaaalaasasmmlmamaasmsmsmamslaasalaslmaalsassaaalmlmmssmlslalslmlmlaasalsmssmmlmmamllaamllamlsmsslamalamlmsmmmamasmamllslllsallasalslmsssasaaasaaalmasllmamssllslsmasallalalasmlsmmsalslalllmlssallaammlmlllaasasslalllsslmmsmlslammlamlmamasmmammsalmaallssallslmsmlamlaallalmaalllmalmamlllmlasslslmmmamllsmaaasmsssaasasssmaamsslmssmlmlamlmsamlaalllsmlsmaasamllsaasmmslamsmsaalalmlaasmsaaamalssmammsasllsalslalasmsssmamasllsasmamalaamasmslsmmlmlmlalamlmalmssmmammmasamlllmaalmasllslalalmlaaamlamsmmaslaslmlsamlalmmsmmlsmllllsmlmmsmssmsllssmsamsaaamsmlasslmmmaslallaaamammmallmmaamlalmllllmmmmmlmmassalsalalasammammlllmlmmsalmmlsaasmsallaamalaaamsmmamsasmmsslasmmmaaasslmlmllmmslllalslllalsaaaasslasmsassmmasmlalmmlsllmmlslslaalsassssalmssaasmsaamssslslmslmmsmssssasmaaslasslsmmsamslsasamsaaalsmallmsmsalllssammalalmaalsmlllslmssmllaamalslaasmssamlaalassmssmsmaamsaalsmllmsssalmaaammmslsalmlsaslslsmaamammmasssssamsamllamasmlsaslmaallsallmlsaammassamslsmlsamaamalsalaslaaslslsllmsalssllasasalllmaaammalassmlllamlsaammslmasamaslmaalassaammlmmlalmmalsmmlmsllsslmlsmmslllslsmlaassmsallmaaamsmaamaammmlallsssmlsmsssmlsasmlmlmssaalammalalaammsmssslsamsmmslalslmssmmsammmaalmslllsalslasallallalalsaalmmasamllllllmaslmasmllssssaamaaamllalmlllaslamslsmmsammmlmsllamslasllamsllamsasmlllalmmlmmslsallsslaalassamssllasmslamssmmmalsmmalalalmmslmslaamassmmslmsamlalmmamlmmllammamasamllllmlaasslamlammalamalasslsaamlammssllllsllsmaasaasalsmsmamaslalasasmmamssamsllslsmamsmsslmmsllalammaamlmmlslsmmsaaallmsslslamsmlamlalasasassssamaamaamaammalmsmssalmssmmmaslssmaamlllsslmaamalmlsmsmsslasalmaaamsllmmamsamllmssmslaaaamasmlsssssamaammlsmlsassaalsalmlmalallmmllsalmlmmlsmmmssmaalassllmamasammlamassmsslamalmssammmsmssallmmallllsasssamsaaaamsaalsalaammsmaamlssaslaslllamllmmlmsammlmaaalmsmsamaasalsaaamalalsaaalalslalmaamasmmmlslsamlsamalalmmmmsmamsaaalsammmslsmsmmsmamsmsmmsmmlmssmslasmmmaamslsmmsllmsamasammmsamslaalaaammmsllmmaslmmlaslsssslmlmmssaslsssmalasaslmsasslmaalamsallasmllsslsalmsmaslamaassslsssmslalssmalaaasammasmlslammmmsllmlmsmsammamslmsslsmsasmsslasssmmmaslsmmlslsllssslassmmmsmlsmsalmasmasllallllalasslmmaaaammllamamlmllfftfffhkhkkffhfkkffkffttkkkhktktkktktkfkttftkkhkhthfthkhktttkfhfhffktkfhtfktthfhhthfkhkkffkhttkftfkhkthhhthkftkffthktkkhkftkhfkfktkfhkftkttkfttttkfkhthhftthfkkfkhkthkfhtffktttttttfkkkkfhtkthtfthhfhtkhhhthffhhhfhhhfkttkkhtkfhfkfhfhhhkhkfkfhkhfkfhhkkhfkthhfftfffthkfthkhhhtfhkhttfktfhhkhhhfhhfhfftfhhhfhttthfkfkftttkhffhhfktkhkthtkttkkhthkfffhfhkthhthkhkhkfkttfhfthktktftkkhfkkfkttfhttfttkkkkhhfktttkkfhkfkhktftktttktkhthktththkthfhhfthfkkhhhkffkhhtkfkkfhhkhkfhtfkfthkkfkfftkfhftkhkhffhhfttkhtkthttkfttthtfhfkfkkhfhhhkttffkhtfffhkfkkhfkhkktkhftfffkkthtfkfhtthfhhfthkfhfttffhfkffthttftftkfkhfkkkkfkktfhkffhfhkffhhhhfhktkkkkkhtkhhhffhhktfkkthttffffhkfthhfttkfthkhhttttfttfhttttkffthttfthfttttthtfkftttffthfkkfhffftftkkfktthfhffkthkftttkhkhthtfhhfkhtffhttkkkhkfthfkktthfhttthkhtthkfhtfhhhfhktffkthttthkhhhtfffkhthhkhhhkfhthfhfhkhhkhhtkfththhkffhfffkkfkfhfhffftttftffhththfthhthfhffkfkkkfffkhkhttfkkthffththffkhttfthkhkkthkftkkfhthhttttffhfhttkhtkhtffffhfkfkhfhkthhtfkhhttfhtkkftfffffhhffkhkhhtfftfhhtfhttfhktftfthhhttkkhhkfftththfttkfhhkhkhtkkthkfhhhhfhtttktfkfhkthtthhhkkhfftthtthtfffhhhftkkhfkhhkkhhkthkkhhkhktkkfttkhhhftthffffhhtktktftkhtkhkthkftfkffktfhtkfhhfhtktttttffhkfhkhtthtftkhtthkkkhhtkthhfffkfhhfkttfftktffhthftfthktkkhfthhfhhtkhkfhkhhthhfkfftffkkktkfhthkhkhkhhkfhhhfhffffhfhffttfftfhkthkfhthffhhthhfhtftkkkhhtttkkftkhhtfhtkhtktfttkttkfhkkhkthkthkfhhkthkhfthkhtftthhkfhhktfkkfkktthkhfhthkthtkhkfhktktkhthfkkkkttthtkfthfhffkhfftftftkkkkkthhkftfftftkthkhhfkftfhkfttkkkkfhththtttkftkfhttfhffhhhkhkhhhtthkkffkktkktkftfkfkfffkfhhkfhffkhtfkffkththfffkfffttkfkhtttkhhkttkhfhffkhktthkththkfftkfhkhhttfhtkfhhttkktfttfhhtffkthtkhthhffhthfkftfkfktftkhfftthktkthkthhtkhkttfthtffhftthtkkthkktthhtfkffkkkhhfffthhhfkhtttffhhhtfhtfffttkttthfftfthtthhkthfhtfhhttthhtkkkhkkhkthhffhkhtkkffhffhhtkffthhhhkkktfkhtffkthffkhhkhtkhhhfhfhkkkkhkhkkfthktfktfhhhthttfhfhhkkhfhffhttktththfhkhfkhhkhfkfftkkhttkkhfhfkftffffkkkfkffthfkhhttthkkfktktfktktfftthfftkfkhtkthkfkfftkkhftthkttfhfhtttfhhtftkththkkththfhfhfkfkhhfkhhtfhhkffkftttfhktkkffhfhhhhkthkkhhktkhtthfkfhkkffhffhhhfkkhfkthkktffhkfthhftttkkthhftffktfhhhhttttfthttfhtfftkkkhhtthftkkttfhftthfhffthkkkftkhkfftfkfhktttkfkhftfhtththkttfkhhkhkkhhfhtttkkkfkktkfkkhhtffkhffkhttttffkttkhfhftffhtthhtkffhhfkftkhtthkhtkfhffttkhkhkthktffkftkfttthfhfttkhhkhkkhkhhhfkkkkkthkfftkkhhhkttthfhtffhftfthfhkfffftffhkffhhtffktfhtkfkffffkktftkkfhtktkththftkhfhkkthfhffftkftffkhtfkkkkkfkkfftftttkftkhththkffhtkkttktttkhkfkfkthhtkfkkftfhkkkfkhhfhhtfkhkkfkfhhhfttfhhfkthfkhhhttttfkhhtfhftffhthkkffthfththththffhffthhthtkhfkhthhktkkkhkhhkhfffkfktkttfhkkkthfhfhhfthhkthhhhtfttkhkffhtthftktftttktkfhthhhkftfhhhftkfhhkhkhtfffhftkfhttthktffhhhhttfftthhhhhhtffhttthkkkfhkhhkhhkfftthhtkhhfkttktkffkhhfktttfhhhhthkkhfkfktkhhkhkttkkhhthffkfkfhkfhhftkhtfftktkfkfftfttthhttftfhthtfhfthhfthffhtttkkkhkftfkthftfkhtthkhfhhfkfkkhfkkkftfkkkhhkkkktkhhttkftthhfftthtkfhthfktfffkttkfffkthfkfkhtffhhhfhhhftkhhtfthkhktkththkfhkhtkhfktkftkkhffhhhkfkktthftfttfkhkkkfhkthhhffhktttffhfkfhtkkfttktkfkfhkhftkkthtfhfkkftftkffhkftfhhhkkfhftftkftkhkhhftkffktktftfhhkkfhffthtkhffffthtftthfkhffkkhkkftfkkfhhkhftfkkhffkhktkkfkfkthttkkffkthttfftkfthffhkttkkhtfthfkfthftfkffkfkkhhkhffkfkfhtktkfkkffhkkkhtfttkfhkkhtktffhkfhhkhkhhtkkhhhhktkhhhthkfkfkftftttttthkhkkkftthhthhfthhfttfthtftkkkfhffkffttkffkhtkffhffkfkhfthkhkfhkthkhhkttffftfftttkhthftktfhhtkhtkhtfffhkhhkfttfftkfhhttthftfthkkhtkkthtfkktkkfhhfhffhkftkffkfhkthfftkffkhtffkhkkfkkkkhfhfthktktktkhtfftkfhkfkhfhfkktktkthfftkhkfffhhhhhfhhtfhfthffkhkffkhhthhhttkhhkkthhfkkfkhkfftkttfkhkkfffkktfhfftktthhffffhthhtkfffthtftkthfkfktktktttkhkkkfhhtktktfthffhktkttktfkttkhkhkffthfkfttththhfhhhtkttkfkthfktkhftthkkkkthkthtftfhkhhhfthkthftkkkthftfkkkhffhkktffkfkhtfhftffhhhtfthftfkkfhhhkffktkffhtkhkhhkfttkktkfkftkhfhhhtfhtttkkhtttfhkkffhffttkffhtkffffhfthftffktkkttfhttkthffkkthkffhkffftthktfhfhftktftffkfkhtftkfhhkhkhffhhftkfktftkfkthkkhhtfkkkhhhkfkhkhhkkthhkfhtffftkhkttfktthhhhffthkkkhkftthttfhfkfktfktfkttttkhfhkftftftktfthhfttttkffftkfthhfttfhthkkkhtfhhhktkkkhffthkfhtktffxccdzxczczzzxddxxxxxczdzdddccxdzzzzxxcddcdzccxxzxzccdxcdczxdcxxczzdxzddxxdzczxczcxxcxcxxccdcxcxxdxxxzdzzcxdxxzzdcxzcxcccxcczcxdzdcxcxxxzxdzcdzcdxxxdxcccxxxcdczzdzxxcxxxzzxxczczzdxzzxcxzzczdcdzcdcxxcxcxxdcdzxcccdxzzzcddxzcdxxcxddcxcccxzzcccddcdzzzxzcddcdxcdxzdxzcdcccddxzdxxczzcczcczccczczdzdxdxzzddxcxxdxzczdcxzdcxdxzddxzzxzdzddzxzcddzdxcdcdzxcdcddcccxxxdxczdxcccdzzdxdxdxczzzdzdcxzzxcdzcdzzzdzzcczdczczxxcxzzzxzccczzxzdzczzxczcxzxczxdccczddxxxccxdccdxdcdxzdzcdczdxddxdcxcdcxdxxxzcxdzzczcdxdxzdxdddxxxzzccdczxxxzcdcddzzzczczxxcxdcdcxzdzdxdzdzzzxcxdczzcddxcdxxczzcddccccxzdzzxcdczcxcxxxxdccxcdxzccdccxzzxxcxzzzdzccxzcddcxcxccdxcdcdddzddxzzxczxxdccdxxxccczdzxxddxxdczcxzzxzdcxdzxzxcxzdczdzxzzzxzccccczzzcdczzzzxxcxzxczcxzxzxzddxcxdzdcddxzdcczxdzcdczzzccxcccdzzddxxzdccxxzxcxxcxzczxdzxxcxxxxcxdcxdzdzzzzdxzdcccxzcccxxccxczxcxxzdcddxdczdxxxczzcddxxxxcdczdcdxcdccdczcczdzdxxczzdczcxzczzczzxczdzzzxzzxcdzxxdxdzccdzdzcddzxcccxcddxzzzzzzzzcxzcdzdxzdccxcccxcxdczzcxxxxcxxcdxdzxczdxzdccxcxzzdzcxzxczxzxccdzcxdddcdcdzxzxxzdcczzdcxcddxxcdxdcdczdxcxzxxzzdxzdzzdzxcddxdcddxcdzzzzxzdcxzxzxdcdcdzdcdxzccczxzzzddxzzdxxcxdzxcczcdcdzczxzdxczxcdzdzddcxxxzddccczxcccxddczczdzcxdcddzzxddzzxdzxzdccxdxcxczczccxzdcddcddzzdxzxczddzzcxczxxxddczxczdzxdxzzddzzxzzccxcdxzdzcxzxdcxdzdzzxdzdzdzxxcczcxxxzccdcxcddczxdddzzzcxdzzcdcdxzczdddxdxdxzczddzdxczcxccddcxxcdzcczcxczcxzdxccxzzxdxcdzczzcdxxdcdzdzzccczddccdczdczcdxdxxzdzzccdzcdczxzcxxxcdzzzcxcxczczzdxxdcdzxxcdxcxxzxccdddccxxdccddzczzzdxxddcccdzdzxxzzxdzzzxxdccxcdcddzdxxzdccxdzddccccdzxzdxcxdxczczcdxxczxzcddxcxxcxdxxzxdzcxdxzxcddcdcxdzzxzcccccxzzxdzzdczdczxxddzzzdzdzcddxczcdcxxxdzccdxxxxzcxdxdcdxcxxzxcdxxxdxzdzxczzxxxdcdcczxxzdzxdccdcdddddczxzxxczcxxcxcczddcccxcddcczzczddxccccxcxccxdccccccddczzdzzxxxddzddzcxxdzczdxddzzxzxzxzdcxddzzzxcxcddddcxczczdxddxczcdzdxzczdzxxcxxzcdxdxzczzccdcxzdxzzzdczzxdxzzxczdcxczdcxzzzcxdcddddxxxdccdzdcxzzcxzczcxzzdcddczczcccdcdcxxcxdddccczcdcczdczxddzxdddxccddxzcdxxxdxccdzdxcxdxddxdzzdxdcdcccddxzdczccddccdczczxzzdzxzccczzxcdddzdddcdzxdzccxzzcxdzcxccxcddcxdzdzccxdxxzxcxcdcxdzdxzccxxdxdcdzxxdxdddzcccdzzcdzdcdxczxdczczdcdczdcxxdxcxxzxzczxzzdzdxzzcxcxczddxczzxczzcdxczzddcdxcxxxxcdzczxczdzcxdxddcddxzdxdzcxzccxxdcxzxcdzddxxxdxxzdcxdcxcccdzxxzzxdxczdddxxxczdxzxzzcdxzcczxxccdxcdddxxdzczddxdcczzdzcdzzzcczcxcdccxzzcdxcxzxxzdzcczzzczddccdzdxczzcczcxxzczxzxdxzxczcdzdzxdcxzczzczcczxdxdzdcxcczzzcddczzxxzdcxxxzzczxxccczxdczdxcxxxdcxzdxcccdxzcczdxczxddxzddxdzxxdddcxxdxdzdxczcxzdcdzzddzdcddcczcxzcdxdcxcdczczcxzcxdzczcdxzdcxccxxzccdxzxxcdczdxzxczzxzxxcdzczzzcxzxdxzxxzdzczdzcczxcxzczdzddcxdcxddxxdxdzxxccxxxzcdddxddczzddzzddzxdxzzzxzxzxcccxxczdxcdzccddzczzdczdcccxczddddczzcdzdddxzccczcxxddczxzcczczddddcdzxdcdcxxdzzzzccxccdxdcxdxdxzzccxdczzdxczccdcczxzxdxcdxdzxzxxcccczxxdzzdzccddcxdzzzzxcxxxddzzzdzdccxdzxczzxdzxxddddcxzddzzxcdccxxzccxzcxzxddccxxddcxdxczxxzdzzxcddzcdcdzczzzdzzdxccxcczzczccxcczzczzcczzczdzzdczdxdxxdccxcxxxdzddxdxxzzxzxcdxxdxdcxxcxcxzdxczdcdzdddxdxczzdzdzzccxzzddcdzddxcdczcdxccczxxxxczxdxxxcxzdczxzdczczxdxxzzxddzcxdccdcczdzxdzzxddcdzczzddczcxxczccczxxczczzzxdxzdxdzdcxxzdxccddzdxczdccxxxdcczdzzzdxdxzdxddxdddxxcdxzdxzcddcxzdcdcdzcxzxdcxcdcxxzdczcxdcxdczcczxdxczczdzzcxzdcdxccxczdxcxxdzzdxczzdxzdzxddcccdccxxxcxzdxccccddzzdcdxccccddxcccxdzzxxczxcdxddcdxczdzxzxcczxzzzzcxcdcczxddczzxxzxczdxzccxxcccxccddcdxcczcxczczxcxcdcdcdzzxzxdxzxcdddxdzzxzxxxzzxzzccdxxdddxxdcdczzdccdcxxcczxzxxczczzxxcxcczzdddzdcdxzxddcdxcccdzdxdccxxcxxdxxxdczzzcxxcdcxxdzxxzzcxzzcdxcxdxczdcdzzdcczcxdczdzxzzxccxxdzdzdzxdxzcdzzxcxdzccdcddzddzxcdczdccxdczxzxxxczdxxcxdzdddczczzxzdxcxzxzczzdxzdzxccccddxzxxxzzdccdzzcddcxxdcxxxcdxxzdcdzzzzddzdcxxxzzdzdxcxzzzzzxcdczzdzxdxxdcdcxxzzdxccczcdccdcxzzzccddcccxzxcdzccccxzzcddcdcdcxzxdzcxddczxcdzdddzcdxcxzxxccczzddccczccdddxdzccxcddzcdzzzxxzcczxcddcdzczddzdxxxxxccczczxxxxxccdcxczzdzczxcxdxzdxxzzcccxcddzczzzdxdcxxxzdxccxzcccdzcxxxcdxcxzzzcdxdzzxxdzdzcczczzzzcdzczzcxxcdcccdxzdzzzzzzcxczxcczdzxdzcdxzdcdcxdxczzzzddddzcdxzzzccdzzxxcdxzxcczzxzzccdxcccxxcdzdzzzzxxxddxxdcxxzxcdxzxxdzdczxxxdcdxxxxdzdxxcddczdxzxcxzxzcxzcz",
    #     "aafexpporasshttkzccdxx"))
