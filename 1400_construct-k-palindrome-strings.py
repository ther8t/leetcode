import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1

        for char in counter:
            if k <= 1:
                break
            if counter[char] > 0 and counter[char] % 2 == 1:
                counter[char] -= 1
                k -= 1

        for char in counter:
            if k <= 1:
                break
            reduction = min(counter[char], k - 1)
            counter[char] -= reduction
            k -= reduction

        odd = 0
        for char in counter:
            if counter[char] == 0:
                continue
            if counter[char] % 2 == 1:
                odd += 1

        return odd in (0, 1)


if __name__ == '__main__':
    print(Solution().canConstruct(s = "annabelle", k = 2))
    print(Solution().canConstruct(s = "leetcode", k = 3))
    print(Solution().canConstruct(s = "true", k = 4))
    print(Solution().canConstruct(s = "banana", k = 4))

