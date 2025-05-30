import collections


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = collections.Counter(s)
        button_order = sorted(counter, reverse=True, key= lambda x: counter[x])
        button_press_count_map = collections.defaultdict(int)

        temp = 0
        for b in button_order:
            button_press_count_map[b] = temp // 9 + 1
            temp += 1

        out = 0
        for char in s:
            out += button_press_count_map[char]

        return out


if __name__ == '__main__':
    print(Solution().minimumKeypresses("aaaaaaaabcdefgggghijkllllllllllmmmnoppponono"))

