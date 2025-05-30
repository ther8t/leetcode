import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        out = ""

        while counter:
            sorted_counter = sorted(counter, key=lambda x: counter[x], reverse=True)
            added = False
            for char in sorted_counter:
                if out and char == out[-1]:
                    continue
                out += char
                added = True
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
                break
            if not added:
                return ""

        return out


if __name__ == '__main__':
    # print(Solution().reorganizeString(s = "aab"))
    # print(Solution().reorganizeString(s = "aaab"))
    print(Solution().reorganizeString(s = "vvvlo"))
