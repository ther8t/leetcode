class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        keeper = {'a': a, 'b': b}

        out = 'dd'
        for i in range(a + b):
            for char in sorted(keeper, key=lambda x: keeper[x], reverse=True):
                if char == out[-1] and char == out[-2]:
                    continue
                else:
                    out += char
                    keeper[char] -= 1
                    break

        return out[2:]


if __name__ == '__main__':
    print(Solution().strWithout3a3b(a = 4, b = 1))
