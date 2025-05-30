import collections


class Solution:
    def numSplits(self, s: str) -> int:
        right_map = collections.defaultdict(int)
        left_map = collections.defaultdict(int)
        good_split = 0

        for char in s:
            right_map[char] += 1

        for index, char in enumerate(s):
            # left string is inclusive till index and right string is from index+1:
            left_map[char] += 1
            right_map[char] -= 1
            if right_map[char] == 0:
                del right_map[char]
            if len(left_map) == len(right_map):
                good_split += 1
            if len(left_map) > len(right_map):
                break

        return good_split


if __name__ == '__main__':
    print(Solution().numSplits("aaaa"))
