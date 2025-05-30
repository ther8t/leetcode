import collections


class Solution:
    def minSwaps(self, s: str) -> int:
        counter = collections.Counter(s)
        if abs(counter['0'] - counter['1']) > 1:
            return -1

        if counter['0'] == counter['1']:
            s_finals = ["", ""]
            for i in range(len(s)):
                s_finals[0] += ("0" if i % 2 == 0 else "1")
                s_finals[1] += ("1" if i % 2 == 0 else "0")
        else:
            s_finals = [""]
            order = ["0", "1"] if counter['0'] > counter['1'] else ["1", "0"]
            for i in range(len(s)):
                s_finals[0] += order[i % 2]

        scores = [0, 0]

        for i in range(len(s)):
            for j in range(len(s_finals)):
                if s_finals[j][i] != s[i]:
                    scores[j] += 1

        if 0 in scores and len(s_finals) == 1: scores.remove(0)
        if not scores:
            return 0

        return min(scores) // 2


    """
    Revision 2:
    Accepted 72%
    
    Simple enough no need to fuss over it.
    """
    def minSwaps(self, s: str) -> int:
        counter = collections.Counter(s)
        zero_count, one_count = counter['0'], counter['1']
        if abs(zero_count - one_count) > 1:
            return -1

        def generate():
            if zero_count > one_count:
                return [[i % 2 for i in range(zero_count + one_count)]]
            elif one_count > zero_count:
                return [[(i + 1) % 2 for i in range(zero_count + one_count)]]
            else:
                return [[i % 2 for i in range(zero_count + one_count)], [(i + 1) % 2 for i in range(zero_count + one_count)]]

        min_swaps = len(s)
        for generated in generate():
            swaps = 0
            for j in range(len(s)):
                if int(s[j]) != generated[j]:
                    swaps += 1
            min_swaps = min(min_swaps, swaps // 2)

        return min_swaps




if __name__ == '__main__':
    print(Solution().minSwaps("111000"))
    print(Solution().minSwaps("010"))
    print(Solution().minSwaps("1110"))
    print(Solution().minSwaps("10"))
