class Solution:
    def platesBetweenCandles(self, s: str, queries):
        n = len(s)

        next_plate = [n] * n
        prev_plate = [-1] * n
        all_stars = [0] * (n + 1)

        for i in range(n):
            if s[i] == "*":
                all_stars[i + 1] = all_stars[i] + 1
            else:
                all_stars[i + 1] = all_stars[i]

        stack = []
        for i in range(n):
            while stack and s[i] == "|":
                popped = stack.pop()
                next_plate[popped] = i
            if s[i] == "*":
                stack.append(i)
            else:
                next_plate[i] = i

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and s[i] == "|":
                popped = stack.pop()
                prev_plate[popped] = i
            if s[i] == "*":
                stack.append(i)
            else:
                prev_plate[i] = i

        out = []
        for lo, hi in queries:
            p, n = next_plate[lo], prev_plate[hi]
            if p > hi or n < lo:
                out.append(0)
                continue
            out.append(all_stars[n + 1] - all_stars[p])

        return out


if __name__ == '__main__':
    print(Solution().platesBetweenCandles(s = "**|*******************|**********************************************|************|*********|*****|*********************************************************************************************|***", queries = [[100, 164]]))
