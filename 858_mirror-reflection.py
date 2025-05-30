class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = 1, 1

        while m * p != n * q:
            n += 1
            m = n * q // p

        m %= 2
        n %= 2
        if not m and n: return 0
        if m and n: return 1
        if m and not n: return 2
        return -1


    # def mirrorReflection(self, p: int, q: int) -> int:
    #     targets_map = {(p, 0): 0, (p, p): 1, (0, p): 2}
    #
    #     m = q / p
    #     x, y = 0, 0
    #     mirror = "bottom"
    #     while (x, y) not in targets_map:
    #         c = y - m * x
    #
    #         if mirror != "left" and (0, c) != (x, y) and 0 <= c <= p:
    #             # left mirror hit
    #             x, y, m = 0, c, -m
    #             mirror = "left"
    #         elif mirror != "right" and (p, m * p + c) != (x, y) and 0 <= m * p + c <= p:
    #             # right mirror hit
    #             x, y, m = p, m * p + c, -m
    #             mirror = "right"
    #         elif mirror != "bottom" and ((0 - c) / m, 0) != (x, y) and 0 <= (0 - c) / m <= p:
    #             # bottom mirror hit
    #             x, y, m = (0 - c) / m, 0, -m
    #             mirror = "bottom"
    #         elif mirror != "top" and ((p - c) / m, p) != (x, y) and 0 <= (p - c) / m <= p:
    #             #top mirror hit
    #             mirror = "top"
    #             x, y, m = (p - c) / m, p, -m
    #
    #         x, y = float('%.5f' % x), float('%.5f' % y)
    #
    #     return targets_map[(x, y)]


if __name__ == '__main__':
    print(Solution().mirrorReflection(68, 29))
    print(Solution().mirrorReflection(p = 2, q = 1))