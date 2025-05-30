from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for index, char in enumerate(s):
            if counter[char] == 1:
                return index
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar(s = "leetcode"))
    print(Solution().firstUniqChar(s = "loveleetcode"))
    print(Solution().firstUniqChar(s = "aabb"))
