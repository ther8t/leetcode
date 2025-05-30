class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        keeper = [['a', a], ['b', b], ['c', c]]

        string = "dd"
        while True:
            keeper.sort(key=lambda x: x[1], reverse=True)
            char_added = False
            for index, (char, count) in enumerate(keeper):
                if (char == string[-1] and char == string[-2]) or count == 0:
                    continue
                char_added = True
                string += char
                keeper[index][1] -= 1
                break
            if not char_added:
                return string[2:]


if __name__ == '__main__':
    print(Solution().longestDiverseString(1, 1, 7))
    print(Solution().longestDiverseString(4, 4, 3))
    print(Solution().longestDiverseString(1, 4, 5))
    print(Solution().longestDiverseString(2, 2, 1))
