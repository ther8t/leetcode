from itertools import accumulate


class Solution:
    def totalStrength(self, strength) -> int:
        n = len(strength)
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        stack = []
        acc = [0] + list(accumulate(accumulate(strength)))

        for i in range(len(strength)):
            while stack and strength[stack[-1]] > strength[i]:
                popped_index = stack.pop()
                next_smaller[popped_index] = i
            stack.append(i)

        stack = []
        for i in reversed(range(len(strength))):
            while stack and strength[stack[-1]] >= strength[i]:
                popped_index = stack.pop()
                prev_smaller[popped_index] = i
            stack.append(i)

        all_sum = 0
        for i in range(len(strength)):
            p = prev_smaller[i]
            n = next_smaller[i]

            left_sum = acc[i] - acc[max(p, 0)]
            right_sum = acc[n] - acc[i]

            all_sum += strength[i] * ((i - p) * right_sum - (n - i) * left_sum)

        return all_sum


    # def totalStrength(self, strength) -> int:
    #     n = len(strength)
    #     next_smaller = [n] * n
    #     prev_smaller = [-1] * n
    #     stack = []
    #
    #     for i in range(len(strength)):
    #         while stack and strength[stack[-1]] > strength[i]:
    #             popped_index = stack.pop()
    #             next_smaller[popped_index] = i
    #         stack.append(i)
    #
    #     stack = []
    #     for i in reversed(range(len(strength))):
    #         while stack and strength[stack[-1]] >= strength[i]:
    #             popped_index = stack.pop()
    #             prev_smaller[popped_index] = i
    #         stack.append(i)
    #
    #
    #     for i in range(n):
    #         ns, ps = next_smaller[i], prev_smaller[i]
    #
    #
    #     return 0

if __name__ == '__main__':
    print(Solution().totalStrength(strength=[1, 3, 1, 2]))
