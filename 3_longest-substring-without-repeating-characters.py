import collections
import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            hashmap = {}
            ending = i
            for j in range(i, len(s)):
                if s[j] not in hashmap:
                    ending = j
                    hashmap[s[j]] = 0
                else:
                    print(hashmap)
                    break
            current_max_length = ending - i + 1
            max_length = current_max_length if current_max_length > max_length else max_length
        return max_length


    """
    Revision 2:
    Accepted : 12%
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        def check():
            counter = collections.Counter(s[:mid])
            if len(counter) == mid:
                return True
            for i in range(mid, len(s)):
                counter[s[i]] += 1
                counter[s[i - mid]] -= 1
                if counter[s[i - mid]] == 0:
                    del counter[s[i - mid]]
                if len(counter) == mid:
                    return True
            return False

        lo, hi = 0, 5 * 10 ** 4
        ans = lo
        while lo < hi:
            mid = (lo + hi) // 2
            if check():
                ans = mid
                lo = mid + 1
            else:
                hi = mid
        return ans


    """
    Revision 2:
    Accepted: 95%
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = -1
        last = collections.defaultdict(int)
        ans = 0
        for index, char in enumerate(s):
            if char not in last:
                last[char] = -1
            lo = max(lo, last[char])
            ans = max(ans, index - lo)
            last[char] = index

        return ans

    """
    Attempt 2:
    Accepted : 27%
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = -1
        n = len(s)
        max_len = 1

        if n in {0, 1}:
            return n

        last_pos = collections.defaultdict(int)

        for index, char in enumerate(s):
            if char in last_pos:
                last_char_pos = last_pos[char]
                lo = max(lo, last_char_pos)
            max_len = max(max_len, index - lo)
            last_pos[char] = index

        return max_len

    """
    Attempt: Fired
    Accepted: 40%
    The idea is to keep a track of all the unique characters by maintaining a set/collection.
    The uniqueness is ensured by the set/collection.
    The thing which we need to ensure is that the occurance of the previous character is ensured to be the latest.
    So in 'abca', {a:0, b:1, c:2} and the next a that comes in updated the lo to be be prev occurance of a + 1 and updates the hi to be the current position.
    
    The only place, I missed the logic was that if lo = 2 and the update to a character makes the lo = 1,
    this should not be allowed because some other character has already updated that to ensure that that character is not repeated again.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        prev_index = collections.defaultdict(int)

        ans = 1
        lo, hi = 0, 0
        for i, c in enumerate(s):
            if c in prev_index:
                lo = max(lo, prev_index[c] + 1)
            prev_index[c] = i
            hi = i
            ans = max(ans, hi - lo + 1)

        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s = "abba"))
    print(Solution().lengthOfLongestSubstring(s = "aab"))
    print(Solution().lengthOfLongestSubstring(s = " "))
    print(Solution().lengthOfLongestSubstring(s = "abcabccbb"))
    print(Solution().lengthOfLongestSubstring(s = "bbbbb"))
    print(Solution().lengthOfLongestSubstring(s = "pwwkew"))
