import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        last_cont, prev_cont = [i for i in range(n)], [i for i in range(n)]
        last, prev = collections.defaultdict(int), collections.defaultdict(int)

        for i in range(n - 2, -1, -1):
            if i + 1 < n and text[i + 1] == text[i]:
                last_cont[i] = last_cont[i + 1]
            if text[i] in last:
                last[text[i]] = i

        for i in range(n):
            if i + 1 < n and text[i + 1] == text[i]:
                prev_cont[i + 1] = prev_cont[i]
            if text[i] in prev:
                prev[text[i]] = i

        max_len = 1
        for i in range(n):
            left, right = prev_cont[i - 1] if i - 1 >= 0 else i, last_cont[i + 1] if i + 1 < n else i

        return 1


    def maxRepOpt1(self, text: str) -> int:
        n = len(text)

        counter = collections.Counter(text)
        window = collections.defaultdict(int)

        def add(c):
            window[c] += 1

        def remove(c):
            window[c] -= 1
            if window[c] == 0:
                del window[c]

        def check():
            nonlocal window
            window = collections.defaultdict(int)
            for i in range(mid):
                add(text[i])

            last_index = mid - 1
            while last_index < n:
                if len(window) == 1:
                    return True
                if len(window) == 2:
                    items = sorted(window.keys(), key=lambda x: window[x])
                    if window[items[0]] == 1 and counter[items[1]] > window[items[1]]:
                        return True
                last_index = last_index + 1
                if last_index < n:
                    add(text[last_index])
                    remove(text[last_index - mid])

            return False

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2 + 1
            if check():
                lo = mid
            else:
                hi = mid - 1

        return lo


    def maxRepOpt1(self, text: str) -> int:




if __name__ == '__main__':
    print(Solution().maxRepOpt1(text = "ababa"))
    print(Solution().maxRepOpt1(text = "aaabaaa"))
    print(Solution().maxRepOpt1(text = "aaaaa"))
