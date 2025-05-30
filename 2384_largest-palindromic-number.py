# Definition for a binary tree node.
import collections


class Solution:
    """
    Attempt #2
    Accepted : 17%
    """
    def largestPalindromic(self, num: str) -> str:
        counter = collections.Counter(num)

        doubles = []
        for digit in ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]:
            count = counter[digit]
            for i in range(count // 2):
                doubles.append(digit)
            counter[digit] -= 2 * (count // 2)

        trailing_zero_count = 0
        for i in range(len(doubles)):
            if doubles[i] == "0":
                trailing_zero_count += 1
                counter["0"] += 2
            else:
                break

        single = []
        for digit in ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]:
            if counter[digit] > 0:
                single.append(digit)
                counter[digit] -= 1
                break
        combined = doubles + single + list(reversed(doubles))

        return ''.join(combined[trailing_zero_count:len(combined) - trailing_zero_count])



if __name__ == '__main__':
    print(Solution().largestPalindromic("444947137"))
    print(Solution().largestPalindromic("00009"))
    print(Solution().largestPalindromic("0000"))
